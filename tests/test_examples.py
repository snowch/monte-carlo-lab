# Copyright © 2026 Christopher Snow
"""Execute every source; check estimator references, conservation and CSV failure paths."""
import contextlib, io, json, os, sys, tempfile, unittest, warnings
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
COURSE=json.loads((ROOT/'src/course.json').read_text())
LESSONS=COURSE['lessons'];ALL=LESSONS+COURSE['applications']

def run(lesson,source=None):
    namespace={'__name__':'__main__'}
    stream=io.StringIO()
    plt.close('all')
    with contextlib.redirect_stdout(stream),contextlib.redirect_stderr(stream),warnings.catch_warnings():
        warnings.simplefilter('ignore',DeprecationWarning)
        warnings.simplefilter('error',RuntimeWarning)
        exec(compile(source or (ROOT/'python'/lesson['code']).read_text(),lesson['code'],'exec'),namespace)
    plt.close('all')
    return namespace,stream.getvalue()

class CourseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runs={}
        for lesson in ALL:
            cls.runs[lesson['slug']]=run(lesson)
        print(f'Executed {len(cls.runs)} complete published sources.',flush=True)
    def ns(self,index):return self.runs[LESSONS[index-1]['slug']][0]
    def test_phone_capture_preserves_data_and_log_scale(self):
        from figure_style import capture_figures
        from matplotlib.ticker import LogLocator
        plt.close('all')
        figure,ax=plt.subplots();line,=ax.plot([1,10,100],[2,3,1]);ax.set_xscale('log')
        with warnings.catch_warnings():
            warnings.simplefilter('ignore',DeprecationWarning)
            wide,narrow=capture_figures()
        self.assertEqual((len(wide),len(narrow)),(1,1))
        np.testing.assert_array_equal(line.get_xdata(),[1,10,100])
        np.testing.assert_array_equal(line.get_ydata(),[2,3,1])
        self.assertEqual(ax.get_xscale(),'log')
        self.assertIsInstance(ax.xaxis.get_major_locator(),LogLocator)
        plt.close('all')
    def test_joint_model_matches_reference_tail_probabilities(self):
        ns=self.ns(25)
        for name,exact in [('independent_total',.125),('shared_total',.25)]:
            values=ns[name];estimate=np.mean(values>70)
            se=np.sqrt(exact*(1-exact)/len(values))
            self.assertLess(abs(estimate-exact),6*se)
    def test_every_example_produces_output_without_warnings(self):
        for lesson in ALL:
            with self.subTest(lesson=lesson['slug']):
                output=self.runs[lesson['slug']][1]
                self.assertTrue(output.strip())
                self.assertNotIn('Warning',output)
                self.assertNotIn('Traceback',output)
    def test_learning_routes_are_complete(self):
        self.assertEqual(len(LESSONS),76)
        self.assertEqual(len(COURSE['applications']),3)
        self.assertEqual(len({l['slug'] for l in ALL}),79)
        self.assertEqual(sum(l['track']=='core' for l in LESSONS),60)
        self.assertEqual(sum(l['track']=='advanced' for l in LESSONS),16)
        for m in range(12):self.assertEqual(sum(l['module']==m for l in LESSONS),6 if m<10 else 8)
        for lesson in ALL:
            self.assertEqual(len(lesson['options']),3)
            self.assertIn(lesson['correct'],range(3))
            self.assertEqual(len(lesson['explain']),3)
            self.assertGreater(sum(len(p.split()) for p in lesson['explain']),95)
            self.assertEqual(len(lesson['hints']),2)
            self.assertTrue(all(lesson[k] for k in ['goal','predict','look','change','feedback','limit','kind','source']))
            self.assertIn('No real-world outcomes were measured',(ROOT/'python'/lesson['code']).read_text())
    def test_attendance_matches_exact_probability_with_sampling_error(self):
        ns=self.ns(1)
        exact=stats.binom.sf(110,150,.72)
        observed=np.mean(ns['attendance']>110)
        se=np.sqrt(exact*(1-exact)/len(ns['attendance']))
        self.assertLess(abs(observed-exact),6*se)
        self.assertTrue(np.all((ns['attendance']>=0)&(ns['attendance']<=150)))
    def test_project_schedule_and_inventory_invariants(self):
        ns=self.ns(39)
        self.assertTrue(np.all(ns['parallel']<=ns['serial']))
        self.assertTrue(np.all(ns['parallel']>=ns['review']))
        ns=self.ns(40)
        self.assertTrue(np.all(ns['stock']>=0))
        self.assertTrue(np.all(ns['pipeline']>=0))
        self.assertTrue(np.all(ns['lost']>=0))
        ns=self.ns(57)
        self.assertTrue(np.array_equal(ns['served']+ns['unmet'],ns['demand']))
    def test_value_of_information_respects_loss_order(self):
        ns=self.ns(53)
        self.assertLessEqual(ns['perfect_information'],ns['best_fixed']+1e-10)
        self.assertGreaterEqual(ns['evpi'],0)
        self.assertTrue(np.all(ns['regret']>=0))
    def test_weighted_rare_event_matches_known_tail(self):
        ns=self.ns(66)
        # Use actual weighted contributions, not the proposal hit fraction.
        values=ns['contribution']
        estimate=values.mean();se=values.std(ddof=1)/np.sqrt(len(values))
        self.assertLess(abs(estimate-stats.norm.sf(5)),6*se)
    def test_mcmc_known_targets_and_diagnostics(self):
        self.assertLess(abs(self.ns(71)['kept'].mean()-20/34),.025)
        self.assertLess(abs(self.ns(72)['chain'][2000:].mean()-20/34),.025)
        ns=self.ns(73)
        self.assertTrue(np.all(np.abs(ns['kept'].mean(axis=0))<.12))
        self.assertLess(abs(np.cov(ns['kept'].T)[0,1]-.85),.2)
        ns=self.ns(74)
        self.assertGreater(ns['ess'],100)
        self.assertLess(ns['ess'],ns['n']/4)
        ns=self.ns(75)
        self.assertLess(ns['diagnostics'](ns['good'])[1],1.01)
        self.assertGreater(ns['diagnostics'](ns['scale_mismatch'])[1],1.05)
    def capstone(self,text=None,case='inventory'):
        source=(ROOT/'python'/LESSONS[59]['code']).read_text().replace('case = "inventory"',f'case = "{case}"')
        previous=os.getcwd()
        try:
            with tempfile.TemporaryDirectory() as directory:
                os.chdir(directory)
                if text is not None:Path('data.csv').write_text(text)
                return run(LESSONS[59],source)
        finally:os.chdir(previous)
    def test_all_capstone_starters_and_uploaded_data(self):
        for case in ['inventory','project','measurement']:
            _,output=self.capstone(case=case)
            self.assertIn('INVENTED starter',output)
            self.assertIn('CASE: '+case,output)
        values=np.arange(10,26,2)
        text='value\n'+'\n'.join(map(str,values))+'\n'
        ns,output=self.capstone(text)
        np.testing.assert_array_equal(ns['values'],values)
        self.assertIn('uploaded CSV',output)
        self.assertNotIn('INVENTED starter',output)
        self.assertTrue(np.all(ns['demand']<50))
        self.assertTrue(all(row['P_shortage']==0 for row in ns['rows']))
    def test_capstone_rejects_invalid_csv(self):
        invalid=['wrong\n1\n2\n','value\n1\n2\n','value\n'+'2\n'*8,
            'value\n1\n2\n3\n4\n5\n6\n7\ninf\n',
            'value\n1\n2\n3\n4\n5\n6\n7\n-1\n',
            'value\n1\n2\n3\n4\n5\n6\n7\nhello\n']
        for text in invalid:
            with self.subTest(text=text),self.assertRaises((AssertionError,ValueError)):self.capstone(text)
if __name__=='__main__':unittest.main()
