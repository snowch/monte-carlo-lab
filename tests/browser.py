# Copyright © 2026 Christopher Snow
"""Drive real Wasm executions, exports, recovery and responsive reading paths."""
import base64, contextlib, json, math, os, re, subprocess, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright
from quiet_checks import check_quiet_layout
ROOT=Path(__file__).resolve().parents[1]
COURSE=json.loads((ROOT/'src/course.json').read_text())
LESSONS=COURSE['lessons']
ALL=LESSONS+COURSE['applications']+[COURSE['introduction']]
CAPSTONE=next(l for l in LESSONS if l['capstone'])
RESULTS=ROOT/'test-results';RESULTS.mkdir(exist_ok=True)
BASE='http://127.0.0.1:5186/monte-carlo-lab/'

def visit(page,url):
    page.goto(url)
    page.wait_for_selector('html[data-ready="true"]')

def wait_result(page):
    page.wait_for_function("document.querySelector('#status').textContent.startsWith('Completed') || document.querySelector('#status').textContent.includes('error') || document.querySelector('#status').textContent.includes('could not')",timeout=150000)
    status=page.locator('#status').inner_text()
    assert status.startswith('Completed'),status+'\n'+page.locator('#error-summary').inner_text()

def open_optional(page,identifier):
    details=page.locator('#'+identifier)
    if not details.evaluate('e=>e.open'):details.locator(':scope > summary').click()

def restore_example(page):
    open_optional(page,'editor-tools')
    page.locator('#restore').click()

def download(page,selector,path):
    if selector=='#download-code':open_optional(page,'editor-tools')
    with page.expect_download() as info:page.locator(selector).click()
    info.value.save_as(path)

def report_block(report,language):
    block=re.search(rb'(?m)^(?P<fence>`{3,})'+language+rb'\n(?P<content>.*?)\n(?P=fence)$',report,re.S)
    assert block,language
    return block['content']

server=subprocess.Popen([sys.executable,'-m','http.server','5186','--bind','127.0.0.1','--directory',str(ROOT/'.preview')],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
try:
    import urllib.request
    for _ in range(50):
        try:
            urllib.request.urlopen(BASE,timeout=1);break
        except Exception:time.sleep(.1)
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path=None if os.environ.get('CI') else os.environ.get('CHROMIUM_PATH','/usr/bin/chromium'),headless=True,args=['--no-sandbox'])
        context=browser.new_context(viewport={'width':1440,'height':1000},accept_downloads=True)
        # No third-party request should be needed for fonts, code, plots or runtime.
        context.route('**/*',lambda route:route.continue_() if route.request.url.startswith('http://127.0.0.1:5186/') or route.request.url.startswith(('data:','blob:')) else route.abort())
        page=context.new_page();errors=[];page.on('pageerror',lambda error:errors.append(str(error)))
        visit(page,BASE)
        assert page.locator('.lesson-row').count()==80
        first=page.locator('#course .lesson-row').first
        assert first.locator('.lesson-number').inner_text()=='00'
        assert first.get_attribute('href')=='lessons/probability-essentials.html'
        assert 'Optional' in first.locator('.lesson-time').inner_text()
        page.locator('#search').fill('probability essentials')
        assert page.locator('.lesson-row:visible').count()==1
        assert first.is_visible()
        assert page.locator('#search-count').inner_text()=='1 investigation'
        page.locator('#search').fill('')
        assert page.locator('.lesson-row h4').first.evaluate('el=>parseFloat(getComputedStyle(el).fontSize)')>=17
        assert page.locator('#start-course').evaluate('el=>parseFloat(getComputedStyle(el).fontSize)')>=16
        assert page.evaluate('getComputedStyle(document.documentElement).backgroundColor')=='rgb(249, 250, 252)'
        assert 'DM Sans' in page.evaluate('getComputedStyle(document.documentElement).fontFamily')
        assert 'Sora' in page.locator('h1').evaluate('(el)=>getComputedStyle(el).fontFamily')
        assert not page.locator('#course-example').evaluate('e=>e.open')
        open_optional(page,'course-example')
        assert '10,000' in page.locator('.model-inputs').inner_text()
        page.locator('#course-example > summary').click()
        page.screenshot(path=str(RESULTS/'overview-desktop.png'),full_page=True)
        page.locator('#search').fill('confidence')
        assert 0<page.locator('.lesson-row:visible').count()<80
        page.locator('#search').fill('no-such-topic-zzzz')
        assert page.locator('#search-empty').is_visible()
        page.locator('#search').fill('')
        # A revision must preserve an existing learner draft while making the
        # current teaching example recoverable without silently replacing it.
        page.evaluate("localStorage.setItem('mcl:v1:draft:see-the-outcomes-before-the-headline:code',\"print('saved learner work')\")")
        visit(page,BASE+'lessons/see-the-outcomes-before-the-headline.html')
        assert page.locator('#code').input_value()=="print('saved learner work')"
        assert page.locator('#saved-draft-note').is_visible()
        restore_example(page)
        assert 'delay = np.array' in page.locator('#code').input_value()
        assert not page.locator('#saved-draft-note').is_visible()
        page.reload();page.wait_for_selector('html[data-ready=true]')
        open_optional(page,'editor-tools')
        page.locator('#recover-draft').click()
        assert page.locator('#code').input_value()=="print('saved learner work')"
        assert page.evaluate('document.activeElement.id')=='code'
        restore_example(page)
        visit(page,BASE)
        # The optional preparation page is executable and portable, but never
        # changes the existing course count or lesson identities.
        assert page.locator('#lesson-zero-link').get_attribute('href')=='lessons/probability-essentials.html'
        page.locator('#lesson-zero-link').click()
        page.wait_for_selector('html[data-ready="true"]')
        assert 'Lesson 0 · Optional' in page.locator('.lesson-context').inner_text()
        assert page.locator('.concept-figure').evaluate('e=>e.previousElementSibling.textContent').startswith('For room overflow')
        assert page.locator('.prelude-note a').inner_text()=='Skip to lesson 1'
        assert page.locator('.prelude-link').get_attribute('aria-current')=='page'
        page.locator('#run').click();wait_result(page)
        assert 'Illustrative fraction: 0.25 = 25.0 %' in page.locator('#output').inner_text()
        source=page.locator('#code').input_value()
        page.locator('#code').fill(source.replace('seats = 2','seats = 1'))
        page.locator('#run').click();wait_result(page)
        assert 'Illustrative fraction: 0.75 = 75.0 %' in page.locator('#output').inner_text()
        restore_example(page)
        page.locator('input[name=answer][value="0"]').check();page.locator('#quiz button').click()
        assert 'reasoning fits' in page.locator('#quiz-feedback').inner_text()
        open_optional(page,'lesson-notes');page.locator('#notes').fill('Probability refresher note')
        page.locator('#mark-read').check()
        page.locator('.prelude-note a').click();page.wait_for_selector('html[data-ready="true"]')
        assert 'Lesson 01 of 76' in page.locator('.lesson-context').inner_text()
        assert page.locator('.lesson-pagination a').first.get_attribute('href')=='probability-essentials.html'
        visit(page,BASE)
        assert page.locator('#progress-count').inner_text()=='0 / 76 read'
        assert page.locator('#course .lesson-row').first.locator('[data-read]').inner_text()=='✓ Read'
        page.evaluate("localStorage.setItem('mcl:v1:read:will-the-room-be-full','true')")
        visit(page,BASE)
        assert page.locator('#start-label').inner_text()=='Continue learning'
        assert page.locator('#start-course').get_attribute('href')=='lessons/'+LESSONS[1]['slug']+'.html'
        # Execute all published sources in one worker. Each run has a fresh
        # namespace; this also checks isolation without paying 79 import costs.
        # Every actual page is checked independently below at narrow widths.
        visit(page,BASE+'lessons/'+LESSONS[0]['slug']+'.html')
        assert not page.locator('#run-result').is_visible()
        assert not page.locator('#stop').is_visible()
        assert not page.locator('#export-run').is_visible()
        assert page.locator('.outcome,.on-this-page,.mobile-course-bar').count()==0
        assert page.locator('.explanation p').first.evaluate('el=>parseFloat(getComputedStyle(el).fontSize)')>=20
        assert page.locator('#code').evaluate('el=>parseFloat(getComputedStyle(el).fontSize)')>=16
        assert page.locator('#output').evaluate('el=>parseFloat(getComputedStyle(el).fontSize)')>=16
        assert page.locator('#code').evaluate('el=>getComputedStyle(el).lineHeight')==page.locator('.code-gutter').evaluate('el=>getComputedStyle(el).lineHeight')
        assert page.locator('#code-editor').evaluate("el=>el.classList.contains('is-highlighted')")
        assert page.locator('#code-highlight .token-keyword').count()>0
        for i,lesson in enumerate(ALL):
            source=(ROOT/'python'/lesson['code']).read_text()
            page.locator('#code').fill(source)
            assert page.locator('#code-highlight code').text_content()==source+'\n'
            page.locator('#run').click();wait_result(page)
            actual=page.locator('#output').inner_text()
            assert len(actual)>10
            if True:
                native=json.loads((ROOT/'.cache/worked.json').read_text())['lessons'][lesson['slug']]['stdout'].strip()
                # Floating formatting across native and Wasm may differ at last digits.
                a_nums=re.findall(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?',actual)
                b_nums=re.findall(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?',native)
                assert len(a_nums)==len(b_nums),(lesson['slug'],actual,native)
                for a,b in zip(a_nums,b_nums):assert math.isclose(float(a),float(b),rel_tol=2e-4,abs_tol=2e-4),(lesson['slug'],a,b)
            record=json.loads((ROOT/'.cache/worked.json').read_text())['lessons'][lesson['slug']]
            assert page.locator('#plots img').count()==len(record['figures'])
            assert page.locator('#plots picture source').count()==len(record['figures'])
            if i==0:
                assert page.locator('#plots img').count()==1
                assert page.locator('.concept-figure').is_visible()
                assert page.locator('.concept-figure').evaluate('e=>[...e.parentElement.children].filter(x=>x.tagName==="P").every(x=>Boolean(x.compareDocumentPosition(e)&Node.DOCUMENT_POSITION_FOLLOWING))'),('diagram precedes explanation',lesson['slug'])
                assert page.locator('.lab-workspace .worked').count()==1
                assert page.locator('#plots a').get_attribute('href').startswith('blob:')
                page.screenshot(path=str(RESULTS/'lesson-desktop.png'),full_page=True)
            if i==3:assert page.locator('#plots img').count()==1
            page.locator('#mark-read').check()
            print(f'PASS Wasm {i+1:02d}: {lesson["slug"]}',flush=True)
        # A policy edit keeps the seed/trials and changes both risk and plot boundary.
        source=(ROOT/'python'/LESSONS[0]['code']).read_text().replace('150, 0.72, 110','150, 0.72, 120')
        page.locator('#code').fill(source);page.locator('#run').click();wait_result(page)
        probability=float(re.search(r'Estimated P\(attendance > seats\): ([\d.]+)',page.locator('#output').inner_text())[1])
        assert 0<probability<.05
        download(page,'#export-run',RESULTS/'attendance-120-run.json')
        edited=json.loads((RESULTS/'attendance-120-run.json').read_text())
        assert edited['source']==source
        assert 'Overflow: above 120' in base64.b64decode(edited['figures_svg_base64'][0]).decode()
        assert len(edited['figures_narrow_svg_base64'])==1
        previous_plot=page.locator('#plots img').get_attribute('src')
        page.locator('#code').fill(source+'\nraise ValueError("after the plot")\n')
        page.locator('#run').click()
        page.wait_for_selector('#run-error')
        assert page.locator('#plots img').get_attribute('src')==previous_plot
        print('PASS edited attendance, exact-source export and plot preservation after a failed run',flush=True)

        # Follow the visible action on each revised lesson with optional help closed.
        for number,old,new in [(14,'6400','10000'),(38,'initial_state = 0','initial_state = 2'),(50,'0.10','0.02')]:
            lesson=LESSONS[number-1]
            visit(page,BASE+'lessons/'+lesson['slug']+'.html')
            assert page.locator('.prepared-state').inner_text()=='Select Run Python below with the code unchanged.'
            assert old in page.locator('.change-task').inner_text() and new in page.locator('.change-task').inner_text()
            assert not page.locator('#editor-tools').evaluate('e=>e.open')
            source=page.locator('#code').input_value()
            page.locator('#run').click();wait_result(page)
            baseline=page.locator('#output').inner_text()
            page.locator('#code').fill(source.replace(old,new,1))
            page.locator('#run').click();wait_result(page)
            changed=page.locator('#output').inner_text()
            if number==14:
                assert 'n: 6400' in baseline and 'n: 6400' not in changed
                errors_by_draws={int(n):float(error) for n,error in re.findall(r'n: (\d+) RMSE across batches: ([\d.]+)',changed)}
                assert .07<errors_by_draws[10000]/errors_by_draws[100]<.13
            elif number==38:
                def proportions(output):
                    return {int(step):[float(value) for value in row.split()] for step,row in re.findall(r'Step (\d+): \[([^\]]+)\]',output)}
                original_rows,changed_rows=proportions(baseline),proportions(changed)
                assert original_rows.keys()==changed_rows.keys()=={1,5,20}
                assert 'Initial state: 0' in baseline and 'Initial state: 2' in changed
                differences=[sum(abs(a-b) for a,b in zip(original_rows[step],changed_rows[step])) for step in (1,5,20)]
                assert differences[0]>differences[1]>differences[2]
            else:
                assert 'Best feasible point-estimate choice: 32' in baseline
                assert 'Best feasible point-estimate choice: 36' in changed
                page.locator('#code').fill(source.replace(old,'0.005',1))
                page.locator('#run').click();wait_result(page)
                assert 'No tested stock level meets the limit based on its estimated shortage probability.' in page.locator('#output').inner_text()
                assert not page.locator('#run-error').is_visible()
        print('PASS original and edited convergence, starting state and shortage limit lessons',flush=True)

        # CSV input must replace starter data; exports preserve executed inputs.
        page.set_viewport_size({'width':390,'height':844})
        visit(page,BASE+'lessons/'+CAPSTONE['slug']+'.html')
        csv='\ufeffvalue\r\n10\r\n12\r\n14\r\n16\r\n18\r\n20\r\n22\r\n24\r\n'
        filename='observations-'+('quarterlydata'*15)+'.csv'
        result_provenance=page.locator('#output-provenance')
        assert 'invented starter data' in page.locator('#input-kind').inner_text()
        assert not page.locator('#csv-upload').is_visible()
        open_optional(page,'observations')
        assert 'at least eight observations' in page.locator('.upload-panel').inner_text()
        assert not page.locator('#clear-csv').is_visible()
        page.evaluate('''() => {
            const read=File.prototype.arrayBuffer;
            File.prototype.arrayBuffer=function(){
                return new Promise(resolve=>{window.finishReading=()=>{
                    window.finishReading=null;
                    resolve(read.call(this));
                };});
            };
        }''')
        picker=page.locator('#csv-upload')
        picker.focus()
        picker.set_input_files({'name':filename,'mimeType':'text/csv','buffer':csv.encode()})
        page.wait_for_function("typeof window.finishReading==='function'")
        assert page.locator('#run').is_disabled() and picker.is_disabled()
        page.evaluate('window.finishReading()')
        page.wait_for_function("name=>document.querySelector('#input-kind').textContent.includes(name)",arg=filename)
        assert page.evaluate('document.activeElement.id')=='csv-upload'
        old_source=page.locator('#code').input_value()+"\n# A Markdown fence: ```\nprint('```')\n"
        page.locator('#code').fill(old_source)
        page.locator('#run').click();wait_result(page)
        original_output=page.locator('#output').inner_text()
        assert 'uploaded CSV' in original_output and 'INPUT OBSERVATIONS: 8' in original_output
        assert 'CSV for this result · '+filename in result_provenance.inner_text()
        assert result_provenance.evaluate('el=>el.scrollWidth<=el.clientWidth')
        page.locator('#report-question').fill('Which stock meets the stated loss and service objective?')
        page.locator('#report-source').fill('Browser test fixture, invented demand observations.')
        download(page,'#export-run',RESULTS/'run.json')
        record=json.loads((RESULTS/'run.json').read_text())
        assert record['input_csv']==csv and record['versions']['scipy']=='1.14.1'
        assert record['source']==old_source and record['error'] is None
        page.locator('#code').fill(old_source+'\n# changed after execution\n')
        assert 'changed' in page.locator('#output-provenance').inner_text()
        download(page,'#export-run',RESULTS/'run-after-edit.json')
        assert json.loads((RESULTS/'run-after-edit.json').read_text())==record
        download(page,'#export-report',RESULTS/'investigation.md')
        report=(RESULTS/'investigation.md').read_bytes()
        assert b'changed after this run' in report and report_block(report,b'csv')==csv.encode()
        print('PASS CSV and exact-source exports',flush=True)
        # Invalid CSV must fail visibly, then recover to starter input.
        restore_example(page)
        picker.set_input_files({'name':'bad.csv','mimeType':'text/csv','buffer':b'wrong,columns\n1,2\n'})
        page.wait_for_function("typeof window.finishReading==='function'")
        page.evaluate('window.finishReading()')
        page.wait_for_function("document.querySelector('#input-kind').textContent.includes('bad.csv')")
        page.locator('#run').click()
        page.wait_for_function("document.querySelector('#status').textContent.includes('reported an error')",timeout=90000)
        assert 'Use your own CSV' in page.locator('#status').inner_text()
        assert 'CSV needs a value column' in page.locator('#error-summary').inner_text()
        assert 'bad.csv' in page.locator('#error-input').inner_text()
        assert filename in result_provenance.inner_text()
        assert page.locator('#output').inner_text()==original_output
        download(page,'#export-run',RESULTS/'run-after-error.json')
        assert json.loads((RESULTS/'run-after-error.json').read_text())==record
        download(page,'#export-report',RESULTS/'investigation-after-error.md')
        report=(RESULTS/'investigation-after-error.md').read_bytes()
        assert filename.encode() in report and b'bad.csv' not in report
        assert report_block(report,b'python')==old_source.encode()
        assert report_block(report,b'csv')==csv.encode()
        assert report_block(report,b'text')==record['stdout'].encode()
        picker.set_input_files({'name':'non-utf8.csv','mimeType':'text/csv','buffer':b'value\n\xff\n'})
        page.wait_for_function("typeof window.finishReading==='function'")
        page.evaluate('window.finishReading()')
        page.wait_for_function("document.querySelector('#csv-status').textContent.includes('Save the CSV as UTF-8')")
        assert 'bad.csv' in page.locator('#input-kind').inner_text()
        page.locator('#clear-csv').click();page.locator('#run').click();wait_result(page)
        assert 'INVENTED starter' in page.locator('#output').inner_text()
        assert not page.locator('#clear-csv').is_visible()
        # Editor error and Stop must leave a viable next action.
        visit(page,BASE+'lessons/'+LESSONS[0]['slug']+'.html')
        page.locator('#code').fill("print('before failure')\nraise ValueError('deliberate test error')")
        page.locator('#code').press('Control+Enter')
        page.wait_for_function("document.querySelector('#status').textContent.includes('reported an error')",timeout=150000)
        assert not page.locator('#run-result').is_visible()
        assert not page.locator('#export-run').is_visible()
        assert 'deliberate test error' in page.locator('#error-summary').inner_text()
        open_optional(page,'error-details')
        assert 'before failure' in page.locator('#error-trace').inner_text()
        page.locator('#code').fill('while True: pass')
        page.locator('#code').press('Tab')
        assert page.evaluate('document.activeElement.id')=='run'
        page.keyboard.press('Enter');page.wait_for_function("document.querySelector('#status').textContent==='Running your Python…'",timeout=30000)
        assert page.locator('#stop').is_visible()
        assert page.evaluate('document.activeElement.id')=='stop'
        page.keyboard.press('Enter');assert 'Stopped' in page.locator('#status').inner_text()
        assert page.evaluate('document.activeElement.id')=='run'
        restore_example(page)
        assert page.locator('#code-highlight code').text_content()==page.locator('#code').input_value()+'\n'
        page.locator('#run').click();wait_result(page)
        print('PASS CSV validation, error and Stop recovery',flush=True)
        # Feedback needs an attempt and respects wrong/correct answers.
        page.locator('#quiz button').click();assert 'Choose an answer' in page.locator('#quiz-feedback').inner_text()
        page.locator('input[name=answer][value="1"]').check();page.locator('#quiz button').click()
        assert 'Reconsider' in page.locator('#quiz-feedback').inner_text()
        page.locator('input[name=answer][value="0"]').check();page.locator('#quiz button').click()
        assert 'reasoning fits' in page.locator('#quiz-feedback').inner_text()
        open_optional(page,'prediction-notes')
        page.locator('#prediction').fill('My saved prediction')
        open_optional(page,'lesson-notes')
        page.locator('#notes').fill('A note to preserve')
        page.locator('#code').fill(page.locator('#code').input_value()+'\n# saved draft')
        download(page,'#download-code',RESULTS/'downloaded.py')
        assert '# saved draft' in (RESULTS/'downloaded.py').read_text()
        page.reload();page.wait_for_selector('html[data-ready=true]')
        assert page.locator('#notes').input_value()=='A note to preserve'
        assert page.locator('#prediction').input_value()=='My saved prediction'
        assert '# saved draft' in page.locator('#code').input_value()
        assert page.locator('#mark-read').is_checked()
        page.locator('#code').evaluate('el=>{el.scrollTop=70;el.scrollLeft=30;el.dispatchEvent(new Event("scroll"))}')
        assert page.locator('#code').evaluate('el=>el.scrollLeft')==page.locator('#code-highlight').evaluate('el=>el.scrollLeft')
        page.set_viewport_size({'width':1440,'height':1000})
        print('PASS feedback and saved drafts',flush=True)
        # Theme persists, mobile has no page-wide overflow, all reading routes work.
        page.locator('#theme').click();assert page.locator('html').get_attribute('data-theme')=='dark'
        page.reload();assert page.locator('html').get_attribute('data-theme')=='dark'
        assert page.evaluate('getComputedStyle(document.documentElement).backgroundColor')=='rgb(16, 26, 43)'
        page.screenshot(path=str(RESULTS/'lesson-dark.png'),full_page=True)
        for width in [390,320]:
            page.set_viewport_size({'width':width,'height':844})
            for lesson in ALL:
                visit(page,BASE+'lessons/'+lesson['slug']+'.html')
                assert page.locator('h1').inner_text()==lesson['title']
                assert page.locator('.concept-figure').is_visible()
                assert page.locator('.concept-figure').evaluate('e=>[...e.parentElement.children].filter(x=>x.tagName==="P").every(x=>Boolean(x.compareDocumentPosition(e)&Node.DOCUMENT_POSITION_FOLLOWING))'),('reference precedes definitions',lesson['slug'])
                clipped=page.locator('.concept-figure svg:visible').evaluate_all('''svgs=>svgs.flatMap(svg=>{const f=svg.getBoundingClientRect();return [...svg.querySelectorAll('text')].flatMap(t=>{const r=t.getBoundingClientRect();return r.left<f.left-1||r.right>f.right+1||r.top<f.top-1||r.bottom>f.bottom+1?[t.textContent]:[]})})''')
                assert not clipped,('diagram label',width,lesson['slug'],clipped)
                assert not page.locator('.concept-figure .math-display:visible').evaluate_all('els=>els.some(e=>e.scrollWidth>e.clientWidth+1)'),('equation fit',width,lesson['slug'])
                assert page.locator('.explanation p').first.evaluate('el=>parseFloat(getComputedStyle(el).fontSize)')>=18
                assert page.locator('#code').evaluate('el=>parseFloat(getComputedStyle(el).fontSize)')>=16
                assert page.locator('#output').evaluate('el=>parseFloat(getComputedStyle(el).fontSize)')>=16
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),(width,lesson['slug'])
                page.locator('#mark-read').check()
            visit(page,BASE)
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),('overview',width)
            if width==390:page.screenshot(path=str(RESULTS/'overview-mobile-dark.png'),full_page=True)
        page.set_viewport_size({'width':390,'height':844})
        page.locator('#theme').click()
        visit(page,BASE+'lessons/'+LESSONS[0]['slug']+'.html')
        page.locator('#course-menu-toggle').click()
        assert page.locator('#course-menu-toggle').get_attribute('aria-expanded')=='true'
        assert page.locator('#course-sidebar').is_visible()
        page.keyboard.press('Escape')
        assert page.locator('#course-menu-toggle').get_attribute('aria-expanded')=='false'
        assert not page.locator('#course-sidebar').is_visible()
        assert page.evaluate('document.activeElement.id')=='course-menu-toggle'
        page.screenshot(path=str(RESULTS/'lesson-mobile.png'),full_page=True)
        visit(page,BASE+'field-notes.html')
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
        print('PASS every lesson at 390px and 320px',flush=True)
        # Larger browser text must reflow rather than force the whole page sideways.
        for width in [1440,390,320]:
            page.set_viewport_size({'width':width,'height':1000})
            for route in ['', 'lessons/'+LESSONS[0]['slug']+'.html', 'field-notes.html']:
                visit(page,BASE+route)
                page.evaluate("document.documentElement.style.fontSize='200%'")
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),('200% text',width,route)
            page.evaluate("document.documentElement.style.fontSize=''")
        page.set_viewport_size({'width':390,'height':844})
        # Portable progress can restore notes in a genuinely fresh browser context.
        visit(page,BASE)
        page.locator('.portable-progress summary').click()
        download(page,'#export-progress',RESULTS/'progress.json')
        assert page.locator('#progress-count').inner_text()=='76 / 76 read'
        fresh=browser.new_context(viewport={'width':1440,'height':1000})
        second=fresh.new_page();visit(second,BASE)
        assert second.locator('#progress-count').inner_text()=='0 / 76 read'
        second.locator('.portable-progress summary').click()
        second.locator('#import-progress').set_input_files(str(RESULTS/'progress.json'))
        second.wait_for_function("document.querySelector('#progress-status').textContent.startsWith('Imported')")
        assert second.locator('#progress-count').inner_text()=='76 / 76 read'
        visit(second,BASE+'lessons/probability-essentials.html')
        assert second.locator('#notes').input_value()=='Probability refresher note'
        assert second.locator('#mark-read').is_checked()
        visit(second,BASE+'lessons/'+LESSONS[0]['slug']+'.html')
        assert second.locator('#notes').input_value()=='A note to preserve'
        visit(second,BASE+'lessons/see-the-outcomes-before-the-headline.html')
        open_optional(second,'editor-tools')
        second.locator('#recover-draft').click()
        assert second.locator('#code').input_value()=="print('saved learner work')"
        print('PASS 200% text, menu and portable progress',flush=True)
        # Static reading does not need JS or any runtime assets.
        reading=browser.new_context(java_script_enabled=False,reduced_motion='reduce')
        static=reading.new_page();requests=[];static.on('request',lambda req:requests.append(req.url))
        for lesson in ALL:
            response=static.goto(BASE+'lessons/'+lesson['slug']+'.html')
            assert response.status==200
            assert static.locator('.explanation p').first.inner_text().startswith(re.split(r'[$`]',lesson['explain'][0])[0])
            assert static.locator('.concept-figure').is_visible()
            assert static.locator('.concept-figure figcaption').inner_text().strip()
            assert static.locator('.katex-error').count()==0
            static.locator('.worked summary').click()
            assert static.locator('.worked pre').inner_text().strip()
        assert not any('/engine/' in url for url in requests)
        assert errors==[],errors
        check_quiet_layout(browser,ROOT,BASE,LESSONS)
        browser.close()
        print('PASS: 80 real Wasm examples including optional lesson 0; native numerical agreement; CSV validation and provenance; feedback; error and Stop recovery; drafts; portable exports; mobile 390/320px; both themes; JavaScript-free reading.',flush=True)
finally:
    server.terminate();server.wait(timeout=10)
