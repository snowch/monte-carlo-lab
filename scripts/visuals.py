# Copyright © 2026 Christopher Snow
"""Lesson-specific visual explanations; reference models, never learner output."""
import html
import numpy as np
from scipy import stats

class Canvas:
 def __init__(self,w,alt,h=320):self.w=w;self.h=h;self.alt=alt;self.parts=[]
 def add(self,s):self.parts.append(s)
 def text(self,x,y,t,anchor='middle'):self.add(f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}">{html.escape(str(t))}</text>')
 def line(self,x,y,X,Y,cls='axis'):self.add(f'<path d="M{x:g},{y:g} L{X:g},{Y:g}" class="{cls}"/>')
 def rect(self,x,y,w,h,cls='tile'):self.add(f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="3" class="{cls}"/>')
 def dot(self,x,y,r=4,cls='point'):self.add(f'<circle cx="{x:g}" cy="{y:g}" r="{r:g}" class="{cls}"/>')
 def finish(self):return f'<svg class="concept-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{html.escape(self.alt,quote=True)}">'+''.join(self.parts)+'</svg>'

def fmt(x):return f'{x/1000:.2g}k' if abs(x)>=1000 else f'{x:.3g}' if abs(x)>=10 else f'{x:.2g}'
def graph(w,caption,xlim,ylim,xlabel,ylabel,curves=(),points=(),vlines=(),hist=None):
 c=Canvas(w,caption);L,R,T,B=86,w-28,42,260
 X=lambda a:L+(a-xlim[0])/(xlim[1]-xlim[0])*(R-L)
 Y=lambda b:B-(b-ylim[0])/(ylim[1]-ylim[0])*(B-T)
 for a in np.linspace(*xlim,5):c.line(X(a),T,X(a),B,'grid');c.text(X(a),B+23,fmt(a))
 for b in np.linspace(*ylim,5):c.line(L,Y(b),R,Y(b),'grid');c.text(L-9,Y(b)+5,fmt(b),'end')
 c.line(L,B,R,B);c.line(L,T,L,B);c.text(L,27,ylabel,'start');c.text((L+R)/2,309,xlabel)
 if hist:
  counts,edges,flag=hist
  for n,a,b in zip(counts,edges,edges[1:]):c.rect(X(a),Y(n),max(.7,X(b)-X(a)-1),Y(0)-Y(n),'hist extreme' if flag(a,b) else 'hist')
 for k,(xs,ys) in enumerate(curves):c.add('<path class="curve curve-'+str(k)+'" d="'+' '.join(('M' if j==0 else 'L')+f'{X(a):.2f},{Y(b):.2f}' for j,(a,b) in enumerate(zip(xs,ys)))+'"/>')
 for a,b,k in points:c.dot(X(a),Y(b),4,'point point-'+str(k))
 for a in vlines:c.line(X(a),T,X(a),B,'reference')
 return c.finish()

def histogram(w,caption,values,xlabel,threshold=None,quantiles=False,count_label='Reference draws'):
 values=np.asarray(values);lo,hi=float(values.min()),float(values.max());span=hi-lo
 # A full observed range is shown, not an unlabelled truncated tail.
 edges=np.linspace(lo-.02*span,hi+.02*span,25)
 if threshold is not None and edges[0]<threshold<edges[-1]:edges=np.unique(np.r_[edges,threshold])
 counts,edges=np.histogram(values,bins=edges)
 lines=[threshold] if threshold is not None else list(np.quantile(values,[.5,.9])) if quantiles else []
 return graph(w,caption,(edges[0],edges[-1]),(0,max(counts)*1.15),xlabel,count_label,vlines=lines,hist=(counts,edges,lambda a,b:threshold is not None and a>=threshold-1e-10))

# Flow diagrams explain an actual mathematical operation, comparison or ledger.
# Text is intentionally short; the caption states the inferential boundary.
FLOWS={
3:('One world, one profit',[('Sample together',r'\text{customers, spending, costs}'),('Calculate in that world',r'\Pi=\text{revenue}-\text{cost}'),('Summarise complete worlds',r'E[\Pi],\quad P(\Pi<0)')],'Keep every input for a trial together. Expected profit and the chance of a loss are different summaries of the same authored outcome model.'),
5:('Replay is not a new replication',[('Same seed + operations',r'\text{same random sequence}'),('Replay the calculation',r'\text{same estimate}'),('Independent replication',r'\text{a fresh random stream}')],'A replay checks computational reproducibility. It does not supply another independent estimate; changing the sequence of random calls can also change later draws.'),
6:('Check the same event two ways',[('Simulate the event',r'\widehat p=\operatorname{mean}(X>110)'),('Independent model reference',r'p=P(X>110)'),('Compare with sampling error',r'\text{allow for run-to-run error}')],'For X binomial with 150 opportunities and attendance probability 0.72, compare the strict overflow event with the exact survival function at 110. Sampling variation remains; agreement is not empirical model validation.'),
15:('Numerical error belongs to an estimator',[('Independent outcomes',r'Y_1,\ldots,Y_n'),('Estimate a model mean',r'\bar Y=\frac1n\sum_iY_i'),('Estimate numerical spread',r'\widehat{\mathrm{MCSE}}=s_Y/\sqrt n')],'The estimated MCSE has the same units as the estimated mean. It concerns independent Monte Carlo draws, not real-world variation or uncertainty about model assumptions.'),
18:('Choose a numerical precision budget',[('State the target',r'\text{mean or event probability}'),('Choose a half-width',r'h'),('Plan, then check',r'n\approx(zs/h)^2')],'In the mean-planning formula, z is the chosen normal critical value, s the supplied SD and h the desired half-width. Probability planning uses a Bernoulli variance bound. A chosen trial count is conditional on those assumptions, not new evidence about the world.'),
19:('A number needs a meaning',[('Quantity',r'48\;\text{arrivals/day}'),('Observation window',r'8\;\text{hours/day}'),('Compatible rate',r'6\;\text{arrivals/hour}')],'The invented input register supplies the units and provenance. Converting units checks arithmetic, not whether the assumed rate describes a real service.'),
21:('Fit, then challenge predictions',[('Input evidence',r'\text{observed durations}'),('Fit a positive distribution',r'\widehat\theta'),('Compare quantiles',r'\text{empirical versus fitted}')],'The fit estimates a lognormal shape with location fixed at zero. A converged fit does not establish the tail or the support; fitted predictions beyond the observed sample need validation.'),
23:('Resample evidence, not new reality',[('Original independent days',r'd_1,\ldots,d_{10}'),('Bootstrap whole days',r'\bar d^{*(1)},\ldots,\bar d^{*(B)}'),('Uncertainty about a mean',r'\text{bootstrap percentile interval}')],'The ten invented daily values are treated as independent and representative; the bootstrap approximates uncertainty about an expectation under that assumption. This is not the spread of tomorrow’s demand; copied rows do not create fresh evidence.'),
24:('Separate scenarios are conditional questions',[('Ordinary scenario',r'P(D>80\mid\lambda=40)'),('Busy scenario',r'P(D>80\mid\lambda=70)'),('Disrupted scenario',r'P(D>80\mid\lambda=100)')],'These authored scenario probabilities are within-scenario risks. No probabilities for which scenario occurs have been supplied, so averaging them equally would introduce a new assumption.'),
26:('One shared condition per world',[('Draw the common condition',r'\log F\sim N(0,0.25^2)'),('Use it in both inputs',r'\begin{gathered}F\to\text{arrivals}\\F\to\text{spending}\end{gathered}'),('Propagate the relationship',r'\begin{gathered}\text{revenue}\\=\text{arrivals}\times\text{spending}\end{gathered}')],'The same factor feeds both inputs in each simulated world. Redrawing it independently for spending changes the joint model and can change the revenue tail.'),
29:('Condition first, then draw',[('Weather',r'P(\text{rain})=0.3'),('Attendance chance',r'p=0.5\;\text{or}\;0.8'),('Event attendance',r'X\mid p\sim\operatorname{Binomial}(100,p)')],'The authored weather state selects the attendance probability for an entire event. Replacing it with the average probability preserves a mean but generally changes the variance and tails.'),
30:('Stress-test dependence, not its probability',[('Hold marginals fixed',r'\mu_A,\sigma_A,\mu_B,\sigma_B'),('Vary the assumed link',r'\rho\in\{-0.5,0,0.5,0.9\}'),('Inspect the decision',r'P(A+B>205\mid\rho)')],'The correlation values are sensitivity scenarios. Reusing base draws helps compare them; it does not supply probabilities for the scenarios.'),
33:('A policy changes shortage and waste',[('Use the same attendance',r'A_i'),('Apply each meal choice',r'\text{shortage}=(A_i-m)_+'),('Count both consequences',r'\begin{gathered}L=12(A_i-m)_+\\+3(m-A_i)_+\end{gathered}')],'The authored penalty rates are pounds per meal. Reusing attendance across policies preserves a matched comparison. A lowest expected loss depends on those chosen consequences.'),
34:('Propagate the input interpretation',[('Uncertain dimensions',r'W,\;H\quad(\mathrm{cm})'),('Calculate within a draw',r'A=WH\quad(\mathrm{cm}^2)'),('Summarise the result',r'P(48\le A\le52)')],'The model uses independent normal dimensions with stated scales. The area distribution inherits those assumptions; a shared calibration offset would require a different joint input model.'),
35:('System logic determines success',[('Component states',r'C_1,C_2,C_3'),('Series: all must work',r'P(\text{success})=\prod_ip_i'),('Parallel: at least one works',r'\begin{gathered}P(\text{success})\\=1-\prod_i(1-p_i)\end{gathered}')],'The exact product formulas here require independent component states. A common failure cause can invalidate them. The logic of the system and the dependence model are separate inputs.'),
36:('An average needs its domain scale',[('Uniform input',r'X\sim U(0,2)'),('Average the integrand',r'E[X^2]=4/3'),('Recover the integral',r'\int_0^2x^2\,dx=2E[X^2]=8/3')],'These exact references use the same finite domain and function as the simulation. Omitting the interval width estimates an average, not the requested integral.'),
39:('Parallel work joins at the slower task',[('Two preparations overlap',r'A\quad\parallel\quad B'),('Both must finish',r'\max(A,B)'),('Then review',r'T=\max(A,B)+R')],'The authored dependency graph allows A and B to overlap but requires both before review. Serial time is A + B + R. Resource limits or a different dependency graph change this model.'),
40:('Keep the daily ledger in order',[('Start of day',r'\text{receive due orders}'),('Serve demand',r'\text{served}=\min(\text{stock},D)'),('Update, then order',r'\text{stock}\gets\text{stock}-\text{served}')],'The source advances the pipeline, serves today’s demand, records lost sales, then places orders with a two-day lead time. Changing the order of these operations changes the inventory process.'),
41:('A customer inherits earlier work',[('Arrival',r'a_i'),('Service can start',r's_i=\max(a_i,f_{i-1})'),('Finish and wait',r'f_i=s_i+v_i,\quad w_i=s_i-a_i')],'One trial is an entire queue of customers. The current customer waits for unfinished earlier service; customer readings within a path are not independent queue experiments.'),
42:('Account for the whole time window',[('Alternate states',r'\text{up}\to\text{repair}\to\text{up}'),('Clip the final segment',r'T_{\rm up}+T_{\rm down}=100'),('Finite-window availability',r'A=\text{up time}/100')],'The authored horizon is 100 time units. The last segment must stop at the horizon. The long-run ratio 10/(10+2) is a reference, not an exact claim about every finite window.'),
43:('Vectorise the same calculation',[('Keep the same inputs',r'x_1,\ldots,x_n'),('Loop or array operations',r'y_i=f(x_i)'),('Verify agreement',r'\operatorname{allclose}(y_{\rm loop},y_{\rm array})')],'Array operations change how the calculation is expressed. They must preserve trial boundaries, shapes and mathematical meaning; matching one checked example is not a general proof for arbitrary code.'),
44:('Compare policies inside the same world',[('Draw uncertain inputs once',r'X_i'),('Evaluate both options',r'L_A(X_i),\quad L_B(X_i)'),('Estimate a paired difference',r'D_i=L_B(X_i)-L_A(X_i)')],'Common random numbers preserve each world across policies. Positive covariance between option losses can reduce variance of their difference; the benefit must be checked for the particular estimator.'),
45:('Give every stratum its own draw',[('Partition the domain',r'[0,1]=\bigcup_h I_h'),('Sample inside each part',r'U_h\sim U(I_h)'),('Weight the stratum means',r'\widehat\mu=\sum_h w_h\bar f_h')],'Stratum weights represent their target probability or domain mass. Equal weights are justified for this source’s equal-width uniform strata, not every stratification.'),
46:('Opposite inputs can offset noise',[('Uniform draw',r'U\sim U(0,1)'),('Paired opposite',r'1-U'),('Average the pair',r'\frac12\{e^U+e^{1-U}\}')],'Both marginal inputs are uniform. The source compares equal function-evaluation budgets. Variance reduction depends on the covariance of the two function values, not on pairing alone.'),
47:('Remove a fluctuation with known mean',[('Known reference expectation',r'E[U]=1/2'),('Fit a coefficient on a pilot',r'\widehat\beta'),('Adjust the main draws',r'Y=e^U-\widehat\beta(U-1/2)')],'The pilot and main sample are separate in the source. The adjustment uses a known expectation and must leave the intended target unchanged; an unjustified reference mean introduces bias.'),
48:('Replicate whole randomised point sets',[('One scrambled set',r'2^{10}=1024\;\text{points}'),('One integral estimate',r'\widehat I_r'),('Independent scrambles',r'\operatorname{SD}(\widehat I_1,\ldots,\widehat I_{20})')],'Points within a Sobol set are deliberately structured, not iid observations. Estimate numerical variability across independent scrambles; 1024 points within one set are not 1024 independent estimates.'),
49:('Name both sides of the loss',[('Unmet demand',r'(D-S)_+'),('Unused stock',r'(S-D)_+'),('Authored loss',r'\begin{gathered}L=10(D-S)_+\\+2(S-D)_+\end{gathered}')],'The two penalty coefficients are decision inputs, not measured constants. Expected loss and shortage probability answer different questions under the same model.'),
50:('Apply the constraint before ranking',[('Evaluate matched worlds',r'\widehat E[L_s]'),('Identify feasible choices',r'\widehat P(D>s)\le0.1'),('Rank feasible choices',r'\arg\min_{s\;\text{feasible}}\widehat E[L_s]')],'The source uses a point-estimate feasibility rule. An estimate just below the limit is not a statistical guarantee that the true model risk meets it; numerical error may need a margin.'),
52:('Find where the recommendation changes',[('Change an assumption',r'\lambda\in\{18,22,26,30,34\}'),('Compare the same options',r's\in\{20,25,30,35,40\}'),('Report a conditional choice',r's^*(\lambda)=\arg\min_sE[L_s\mid\lambda]')],'The result maps assumed demand to a preferred policy. It is a sensitivity boundary, not evidence assigning probabilities to the demand scenarios.'),
53:('Information can change the chosen action',[('Best fixed expected loss · A',r'\min_a E[L(a,X)]'),('Perfect-information expected loss · B',r'E[\min_aL(a,X)]'),('Value before information cost',r'\mathrm{EVPI}=A-B')],'Perfect information can choose an action after seeing the world. Its value is an upper bound for this action set and loss model, before the cost of information; it is not a guarantee of achievable value.'),
54:('Decide using only available information',[('Receive a noisy signal',r'Z'),('Apply a prespecified policy',r'S=\pi(Z)'),('Evaluate in the same world',r'L(\pi(Z),D)')],'The adaptive policy sees the simulated signal, not future demand itself. Comparing against a fixed action must respect what is known at decision time.'),
55:('Solve a boundary case by hand',[('No demand, stock 5',r'L(0,5)=10'),('Exact match',r'L(5,5)=0'),('Demand 8, stock 5',r'L(8,5)=30')],'These exact checks follow the authored shortage penalty 10 and leftover penalty 2. Boundary checks can catch accounting errors; they do not validate the demand distribution.'),
56:('Hold evidence outside the fit',[('Specify the input model',r'D\sim\operatorname{Poisson}(20)'),('Predict a threshold',r'q_{0.9}'),('Compare held-out observations',r'\operatorname{mean}(d_{\rm holdout}\le q_{0.9})')],'A precise simulation of a fitted or assumed model is a different check from prediction on held-out observations. The small invented holdout has its own sampling variability.'),
57:('Conserve demand at the boundaries',[('Demand and stock',r'D\ge0,\quad S\ge0'),('Serve what is possible',r'\text{served}=\min(D,S)'),('Check both ledgers',r'\text{served}+\text{unmet}=D')],'The source also requires remaining stock to be nonnegative. These invariants hold at zero demand, zero stock and extreme demand; they test arithmetic independently of distribution fit.'),
58:('Spawn streams, not duplicate seeds',[('Record a parent seed',r'\operatorname{SeedSequence}(2026)'),('Spawn child streams',r'G_1,G_2,G_3,G_4'),('Replay the same spawn tree',r'\text{same child sequences}')],'The source uses SeedSequence.spawn to create separate reproducible child streams. Starting every worker with the same seed would duplicate draws rather than add independent numerical evidence.'),
59:('Keep the finding conditional',[('State the target and model',r'\begin{gathered}P(D>32)\\D\sim\operatorname{Poisson}(25)\end{gathered}'),('Record the calculation',r'\text{trial count, estimate, MC interval}'),('State unresolved evidence',r'\text{input model and penalties}')],'The interval describes numerical uncertainty conditional on the simulation model. It does not establish that Poisson demand or the decision penalties describe reality.'),
60:('Preserve a complete investigation',[('Plan before comparing results',r'\text{question, inputs, model, rule}'),('Execute and verify',r'\text{source, data, versions, checks}'),('Report the finding and scope',r'\text{result, MC error, limits}')],'Inventory, project and measurement starters require different units and target quantities. Upload validation checks CSV structure, not independence or provenance; preserve the exact input and executed run.'),
63:('Return proposal draws to the target',[('Draw from the proposal',r'X_i\sim q'),('Account for the changed law',r'w_i=p(X_i)/q(X_i)'),('Average weighted contributions',r'\widehat\mu=\frac1n\sum_iw_if(X_i)')],'Ordinary importance sampling here uses a normalised target, full proposal support where the integrand matters, and valid weighted variance. The unweighted proposal average answers a different question.'),
64:('Weights cannot fill a missing region',[('Restricted proposal',r'q(x)=0\quad(x>1/2)'),('Missing target contribution',r'\int_{1/2}^1x^2\,dx>0'),('A full-support mixture',r'q(x)=0.2+1.6\,\mathbf1_{x\le1/2}')],'The target integral is over [0,1]. A restricted proposal estimates only its supported contribution. The corrected mixture density must include both routes to a draw. The displayed density applies on [0,1] and is zero elsewhere.'),
66:('More proposal hits are not more target risk',[('Target event',r'P(Z>5),\quad Z\sim N(0,1)'),('Sample nearer the event',r'X\sim N(5,1)'),('Return to the target scale',r'\widehat p=\operatorname{mean}(\mathbf1_{X>5}w(X))')],'The proposal makes rare hits frequent. Correct density-ratio weights restore the target probability; proposal hit rate alone estimates the wrong event distribution.'),
67:('A few weights can control the estimate',[('Normalised weights',r'\widetilde w_i=w_i/\sum_jw_j'),('Concentration diagnostic',r'\mathrm{ESS}_w=1/\sum_i\widetilde w_i^2'),('Weighted result',r'\widehat\mu=\sum_i\widetilde w_if(X_i)')],'Weight ESS is a concentration diagnostic, not a precision guarantee. Self-normalisation has finite-sample ratio bias; repeated runs and target checks still matter.'),
68:('A ratio can remove an unknown constant',[('Unnormalised target',r'\widetilde p(x)\propto e^{-x^4/4}'),('Normalise relative weights',r'\widetilde w_i\propto\widetilde p(X_i)/q(X_i)'),('Self-normalised expectation',r'\widehat\mu=\frac{\sum_iw_iX_i^2}{\sum_iw_i}')],'The unknown target normalising constant cancels. The finite-sample estimator remains a random ratio; an iid SE of raw X squared values would ignore that structure.'),
70:('Posterior uncertainty versus MC error',[('Independent posterior draws',r'p_i\sim\operatorname{Beta}(20,14)'),('Posterior event probability',r'\widehat r=\operatorname{mean}(p_i>0.6)'),('Numerical standard error',r'\widehat{\mathrm{MCSE}}=s_{\rm indicator}/\sqrt n')],'The posterior SD describes uncertainty in p under the chosen prior and likelihood. MCSE describes error in the estimated posterior event probability; more draws reduce numerical error, not posterior uncertainty.'),
72:('Include the reverse proposal probability',[('Propose a candidate',r'y\sim q(\cdot\mid x)'),('Correct the asymmetry',r'\alpha=\min\left(1,\frac{\pi(y)q(x\mid y)}{\pi(x)q(y\mid x)}\right)'),('Accept or retain the old state',r'x_{t+1}=y\;\text{or}\;x_t')],'The source is an independence proposal, so the correction uses q(current)/q(proposed). Dropping or reversing it changes the algorithm and its target.'),
73:('Use the newest coordinate',[('Current state',r'(x_t,y_t)'),('Update the first conditional',r'x_{t+1}\sim p(x\mid y_t)'),('Then the second',r'y_{t+1}\sim p(y\mid x_{t+1})')],'The Gaussian Gibbs sampler uses the latest first coordinate in its second update. Strong correlation can make movement slow, so retained rows are not independent samples.'),
74:('Rows are not an independent count',[('Serially dependent draws',r'X_1,\ldots,X_n'),('Mean-specific effective size',r'\mathrm{ESS}\approx n/\tau'),('Adjusted mean SE',r'\mathrm{SE}(\bar X)\approx s/\sqrt{\mathrm{ESS}}')],'Here τ summarises serial correlation for the mean. For the authored AR(1) model, the long-run approximation is ESS ≈ n(1−ρ)/(1+ρ). Estimating ESS does not establish that an arbitrary MCMC chain reached its target.'),
75:('Compare location and scale across chains',[('Split multiple chains',r'\text{compare within and between}'),('Rank-normalise and fold',r'\widehat R_{\rm rank},\quad\widehat R_{\rm folded}'),('Inspect more than agreement',r'\text{traces, ESS, target exploration}')],'The constructed collections illustrate a diagnostic failure: raw split R-hat can miss scale disagreement. A near-one diagnostic alone is not proof of convergence or exploration.'),
76:('A future group includes parameter uncertainty',[('Draw an uncertain parameter',r'p\sim\operatorname{Beta}(20,14)'),('Draw a future group',r'K\mid p\sim\operatorname{Binomial}(20,p)'),('Keep the targets distinct',r'\begin{gathered}\text{parameter }p\\\text{future count }K\end{gathered}')],'A plug-in forecast fixes p at its posterior mean and discards parameter variation. Predictive count quantiles, posterior parameter intervals and numerical MC error describe different quantities.'),
77:('Keep demand, capacity and cost together',[('One demand world',r'D_i'),('Apply a fixed fleet choice',r'\text{capacity}_a,\quad\text{shortage}_{ia}'),('Count the five-year costs',r'\begin{gathered}C_{ia}=\text{installed cost}\\+\text{operating cost}\end{gathered}')],'The optional workbook compares fixed fleets under shared demand. Its required-unit diagnostic does not silently buy extra capacity; totals are nominal undiscounted five-year model costs.'),
78:('Schedule and cost share the same world',[('Sample a migration path',r'T_i'),('Account for overlap',r'\begin{gathered}C_i=\text{migration}\\+\text{dual-running cost}\end{gathered}'),('Evaluate joint success',r'\mathbf1_{T_i\le d\;\land\;C_i\le b}')],'The workbook keeps each world’s completion and cost together. Multiplying marginal success probabilities would erase their dependence; delays affect dual-running costs.'),
79:('Account for all time, not only useful work',[('Useful work is fixed',r'20\;\text{hours}'),('Add checkpoint overhead',r'\text{completed checkpoints}'),('Include failed attempts',r'\begin{gathered}\text{elapsed}=\text{useful}\\+\text{overhead}+\text{lost work}\end{gathered}')],'The checkpoint workbook repeats interrupted work and includes successful checkpoint overhead. A policy comparison must preserve exactly twenty hours of useful completed work, under the stated interruption model.')
}

def image(index,w,ns):
 title='See the model';caption='';formula=None;legend=[]
 if index==0:
  seats=ns['seats'];events=ns['events'];c=Canvas(w,'Four invented events. Each row contains all three guest decisions. One of the four events exceeds two seats.',h=270)
  c.text(12,25,'Event','start');c.text(w*.45,25,'Guests');c.text(w*.83,25,'Result')
  for i,guests in enumerate(events):
   y=72+i*52;c.text(28,y+7,i+1)
   for j,value in enumerate(guests):
    x=w*(.32+j*.13);c.rect(x-17,y-18,34,36,'tile tile-1' if value else 'tile');c.text(x,y+7,value)
   count=sum(guests);c.text(w*.83,y+7,f'{count} · '+('Over' if count>seats else 'Fits'))
  caption='Each row is one complete invented event: 1 attends and 0 is absent. Only three attendees exceed two seats. One overflow in four rows is 1/4, or 25%. These hand-picked examples teach counting; they are not random samples from the 72% attendance model.'
  return dict(title='Two seats. Which complete events overflow?',caption=caption,svg=c.finish())
 if index==25:
  x=np.linspace(40,80,161);independent=np.where(x<=60,(x-40)/400,(80-x)/400);shared=np.full_like(x,1/40)
  caption='Exact density references for the two authored models. Independent inputs produce a triangular total; sharing one uniform input produces a uniform total. Both means are 60, but the probability above the line at 70 is 0.125 versus 0.25. These are model calculations, not measured evidence.'
  return dict(title='The same mean can hide different tails',caption=caption,legend=['Independent inputs','Shared input'],formula=r'E[A+B]=60\quad\text{in both models}',svg=graph(w,caption,(40,80),(0,.06),'Total (model units)','Density',curves=[(x,independent),(x,shared)],vlines=[70]))
 if index in (1,4,20,31,32,51):
  key={1:'attendance',4:'delay',20:'simulated',25:'independent_total',31:'finish',32:'total_cost',51:'loss'}[index]
  values=ns[key]
  if index==1:
   title='Overflow is an event, not an average';threshold=ns['seats']+.5;label='Attendees per event';caption=f'Seeded published reference: {len(values):,} events with {ns["invited"]} independent invitations at chance {ns["probability"]:g}. Highlighted bars count attendance strictly above {ns["seats"]}; exactly that many guests still fit. This is an assumed attendance model, not measured turnout.';formula=r'\widehat P(X>c)=k/n';caption+=' Here k counts overflow events and n counts all simulated events.'
   edges=np.arange(values.min()-.5,values.max()+1.5);counts,edges=np.histogram(values,bins=edges)
   svg=graph(w,caption,(edges[0],edges[-1]),(0,counts.max()*1.15),label,'Simulated events',vlines=[threshold],hist=(counts,edges,lambda a,b:a>=threshold))
  else:
   title={4:'A tail can move the mean',20:'Resampling inherits its support',25:'A similar mean can hide different tails',31:'A deadline cuts through the distribution',32:'A reserve follows a coverage target',51:'Look beyond the average loss'}[index]
   threshold={4:None,20:80,25:70,31:ns.get('deadline'),32:ns.get('baseline'),51:ns.get('p95')}[index]
   label={4:'Delivery delay (days)',20:'Demand',25:'Combined model outcome',31:'Completion (days)',32:'Total cost (£)',51:'Loss (model units)'}[index]
   caption={4:'Ten invented delivery delays over their full range. Most values are small; the one long delay lifts the mean above the median. The lines mark median 3 and interpolated P90 6 days. These are supplied examples, not simulated or measured evidence.',20:'Actual resampled values from the ten invented observations. No simulated draw can create an unobserved value outside the empirical support. This cannot establish that larger real demand is impossible.',25:'Independent-case reference from the published source. The shared-input model in the code has a different tail despite a similar mean. Independence is a joint-model assumption, not a consequence of matching marginal inputs.',31:'Published task-duration model. The marked deadline is 16 days; its success event includes the boundary. The full completion-time distribution comes from adding task durations within each world.',32:'Published cost model. The marked baseline is £2,500; the reserve calculation instead targets its P90. Neither the baseline nor the chosen coverage target is learned automatically from the simulated draws.',51:'Published lognormal-loss reference, showing the full observed range and its P95 boundary. The mean of observations at or above P95 is the stated empirical tail convention, not a guarantee about the unseen tail.'}[index]
   svg=histogram(w,caption,values,label,threshold,quantiles=index==4,count_label='Invented delays' if index==4 else 'Reference draws')
  return dict(title=title,caption=caption,formula=formula,svg=svg)
 if index==2:
  a=ns['guest_attends'];c=Canvas(w,'Each row is one simulated event; each column is one invited guest.',h=370);left=44;cell=(w-70)/8
  for i in range(6):
   c.text(23,49+i*46,str(i+1))
   for j in range(8):c.rect(left+j*cell,26+i*46,cell-4,30,'tile tile-1' if a[i,j] else 'tile')
  c.text(w/2,341,'8 guest outcomes per row');caption='Actual six-event reference matrix: mint cells attend, pale cells do not. Count guests across each row before deciding whether that event overflows. A guest fraction and an event-overflow fraction are different targets.';c.alt=caption
  return dict(title='One row, one complete event',caption=caption,svg=c.finish())
 if index in (7,65):
  if index==7:values=ns['probabilities'];labels=['Standard','Vegetarian','Premium'];caption='The authored categorical input weights are 0.5, 0.3 and 0.2. These are model probabilities, not the finite simulated frequencies. A separate mapping assigns a cost to each selected category.';title='A probability is a width of the choice space'
  else:values=ns['weights'];labels=['Weight 1','Weight 2','Weight 3'];caption='Actual stable normalised weights from the constructed log values −1001, −1000 and −999. Subtracting log-sum-exp preserves relative weights; direct exponentials underflow. The displayed weights sum to one.';title='Keep relative weights when absolute values underflow';formula=r'\widetilde w_i=\exp(\ell_i-\operatorname{logsumexp}(\ell))'
  c=Canvas(w,caption,h=310);L,R=28,w-28
  for j,(label,v) in enumerate(zip(labels,values)):
   y=52+j*82;c.text(L,y-14,f'{label} · {v:.3g}','start');c.rect(L,y,(R-L)*float(v),32,'tile tile-'+str(j%2))
  return dict(title=title,caption=caption,formula=formula,svg=c.finish())
 if index in (8,9,10,11,12,22,27,61,62,69):
  if index==8:
   x=np.arange(0,ns['n']+1);y=stats.binom.pmf(x,ns['n'],ns['p']);xl='Successes in group';yl='Probability mass';limits=(0,ns['n']);title='A bounded count of successes';caption='Exact binomial input model: 30 independent opportunities with success chance 0.95 each. Integer outcomes range from zero to 30. The mean n·p and variance n·p·(1−p) follow those assumptions.';formula=r'X\sim\operatorname{Binomial}(n,p)'
  elif index==9:
   x=np.arange(11);y=stats.poisson.pmf(x,ns['expected_count']);xl='Arrivals per half-hour';yl='Probability mass';limits=(0,10);title='Scale the rate to the observation window';caption='Exact Poisson reference for 4 arrivals per hour over 0.5 hours: expected count 2. The plotted range is 0–10, but Poisson support has no finite upper bound.';formula=r'\lambda_{\rm window}=4\times0.5=2'
  elif index==10:
   x=np.linspace(0,2,150);y=np.exp(-ns['rate_per_hour']*x);xl='Wait (hours)';yl='P(wait > time)';limits=(0,2);title='Rate and waiting scale are reciprocals';caption='Exact survival curve for the authored exponential rate of 3 per hour. Its mean wait is 1/3 hour; the curve is an interval-tail probability, not probability at one exact time.';formula=r'E[T]=1/\lambda'
  elif index==11:
   x=np.linspace(-8,8,150);y=stats.norm.pdf(x,0,2);xl='Sensor error';yl='Density';limits=(-8,8);title='Symmetry does not justify the support';caption='Exact N(0, 2²) error-model density. Negative sensor errors are meaningful, but an unbounded normal duration model can generate impossible negative times. Density height is not a point probability.';formula=r'E\sim N(0,2^2)'
  elif index==12:
   x=np.linspace(.01,60,180);y=stats.lognorm.pdf(x,s=ns['log_sd'],scale=np.exp(ns['log_mean']));xl='Positive outcome';yl='Density';limits=(0,60);title='The parameters live on the log scale';caption='Exact lognormal reference from the source: log mean log(10), log SD 0.7. The median is 10 and the mean is larger. The model is positive and unbounded; the graph shows only 0–60.';formula=r'\operatorname{median}(X)=e^\mu,\quad E[X]=e^{\mu+\sigma^2/2}'
  elif index==22:
   x=np.linspace(ns['low'],ns['high'],160);y=stats.triang.pdf(x,(ns['mode']-ns['low'])/(ns['high']-ns['low']),loc=ns['low'],scale=ns['high']-ns['low']);xl='Duration (days)';yl='Density';limits=(ns['low'],ns['high']);title='A hard limit comes from the assumption';caption='Exact triangular input model with minimum 2, mode 4 and maximum 12 days. Zero density beyond 12 is imposed by the expert-model assumption; it is not evidence that a real overrun cannot occur.';formula=r'E[T]=(2+4+12)/3=6'
  elif index==27:
   x=np.linspace(-2,2,140);y=np.abs(x);xl='X';yl='Y = |X|';limits=(-2,2);title='Zero correlation can hide a complete relationship';caption='Exact relationship in the authored model: Y is determined by |X|. A near-zero linear correlation cannot summarise this V-shaped dependence.';formula=r'Y=|X|'
  elif index==61:
   x=np.linspace(0,.99,160);y=-ns['scale']*np.log1p(-x);xl='Uniform input u';yl='Transformed wait';limits=(0,1);title='Map probability to a target quantile';caption='Exact inverse-CDF transform for exponential scale 2. Uniform inputs near one generate large waits. The shown range stops at 0.99; the target has no finite upper bound.';formula=r'F^{-1}(u)=-2\log(1-u)'
  elif index==62:
   x=np.linspace(0,1,100);y=2*x;xl='Proposal x';yl='Density';limits=(0,1);title='Accept under a valid envelope';caption='Reference target density 2x on [0,1]. A uniform proposal with envelope multiplier 2 is accepted with probability x. The dashed envelope dominates the target; accepted values have mean 2/3.';formula=r'P(\mathrm{accept}\mid x)=\frac{2x}{2\cdot1}=x'
  else:
   x=np.linspace(.001,.999,180);y=stats.beta.pdf(x,ns['post_a'],ns['post_b']);xl='Unknown probability p';yl='Density';limits=(0,1);title='Evidence updates a probability model';caption='Exact beta densities for the invented 18 successes in 30 trials. The dashed prior is Beta(2,2); the posterior is Beta(20,14). This posterior concerns p, not the next group count.';formula=r'\operatorname{Beta}(a+s,b+n-s)'
  curves=[(x,y)];legend=[]
  if index==62:curves.append((x,np.full_like(x,2)));legend=['Target density','Proposal × envelope multiplier']
  if index==69:curves.append((x,stats.beta.pdf(x,ns['a'],ns['b'])));legend=['Posterior density','Prior density']
  svg=graph(w,caption,limits,(0,max(max(v) for _,v in curves)*1.15),xl,yl,curves=curves,points=[(a,b,0) for a,b in zip(x,y)] if index in (8,9) else [])
  return dict(title=title,caption=caption,formula=formula,legend=legend,svg=svg)
 if index in (13,14,16,17,28,37,38,71):
  if index==13:
   title='Outcome spread stays; mean error shrinks';caption='Reference normal model with mean 100 and SD 20. The long line is ±1 SD for an individual outcome; the short line is ±1 sampling SD of a mean of 400 independent outcomes. Neither is a 95% interval.';c=Canvas(w,caption,h=290);X=lambda a:36+(a-60)/80*(w-72)
   for y,lo,hi,label,k in [(85,80,120,'Individual outcome · SD 20',0),(185,99,101,'Mean of 400 · SD 1',1)]:c.text(26,y-23,label,'start');c.line(X(lo),y,X(hi),y,'interval curve-'+str(k));c.dot(X(100),y)
   for a in [60,80,100,120,140]:c.text(X(a),244,str(a))
   c.text(w/2,282,'Outcome units');formula=r'\mathrm{SD}(\bar X)=\sigma/\sqrt n';return dict(title=title,caption=caption,formula=formula,svg=c.finish())
  if index==14:
   x=np.linspace(100,6400,160);y=np.sqrt(4/45/x);caption='Analytical standard-error curve for independent averages of U², with U uniform on [0,1]. Increasing draws by four halves typical error. A particular running estimate need not improve monotonically; its actual trace appears in the Python output.';formula=r'\mathrm{SE}(\overline{U^2})=\sqrt{4/(45n)}';return dict(title='A typical rate, not a promise for one trace',caption=caption,formula=formula,svg=graph(w,caption,(0,6400),(0,.035),'Independent draws n','Model standard error',curves=[(x,y)]))
  if index==16:
   mean,margin=ns['mean'],ns['margin'];rows=[('95% MC interval for mean',mean-margin,mean+margin),('Central 95% of outcomes',*np.quantile(ns['waits'],[.025,.975]))];caption='Published exponential reference. The short interval concerns the model expectation; the long percentile range concerns individual waits. More draws reduce numerical uncertainty about the mean, not the spread of waits.';formula=r'\bar Y\pm1.96\,s_Y/\sqrt n'
  elif index==17:
   rows=[('Two-sided 95% interval',ns['interval'].low,ns['interval'].high),('One-sided 95% bound',0,ns['one_sided_upper'])];caption='Constructed record: zero failures in 1,000 independent binomial trials. The exact two-sided interval and one-sided upper bound are positive. Their confidence conventions differ; observing zero is not proof of no risk.';formula=r'\text{one-sided upper}=1-0.05^{1/n}'
  elif index==28:
   p=ns['paired'][::80];caption='Published seeded standardised normal draws, displaying every 80th point without selecting by outcome. The target correlation is 0.7. Rescaling each coordinate changes covariance and units while preserving this linear correlation.';svg=graph(w,caption,(-4,4),(-4,4),'Standardised input A','Standardised input B',points=[(float(a),float(b),0) for a,b in p]);return dict(title='Share one normal input, add fresh variation',caption=caption,formula=r'B=\rho Z_1+\sqrt{1-\rho^2}Z_2',svg=svg)
  elif index==37:
   paths=ns['paths'][:3];caption='First three paths of the seeded published walk. Each line contains one hundred dependent positions. Finishing at or above 10 and ever reaching 10 are different events defined on a whole path.';lo=min(-12,float(paths.min()));hi=max(12,float(paths.max()));return dict(title='A path has more than a final state',caption=caption,svg=graph(w,caption,(1,100),(lo,hi),'Step','Position',curves=[(np.arange(1,101),p) for p in paths]))
  elif index==38:
   m=ns['transition'];caption='The authored transition matrix, ordered clear, cloudy, wet. Each row is a probability distribution for the next state conditional on the current state, so its entries sum to one.';return dict(title='Read a row after fixing the current state',caption=caption,kind='table',headings=['Current → next','Clear','Cloudy','Wet'],rows=[[name]+[f'{v:.2f}' for v in row] for name,row in zip(['Clear','Cloudy','Wet'],m)])
  else:
   chain=ns['chain'][:80];caption='First eighty iterations of the actual seeded Metropolis reference, including warm-up. Flat segments retain rejected states; removing them would change the chain. A trace alone cannot certify convergence.';return dict(title='Rejection still produces a recorded state',caption=caption,svg=graph(w,caption,(0,79),(0,1),'Iteration, warm-up included','Parameter p',curves=[(np.arange(80),chain)]))
  hi=max(row[2] for row in rows)*1.15;c=Canvas(w,caption,h=290);X=lambda a:32+a/hi*(w-84)
  for j,(label,a,b) in enumerate(rows):y=82+j*95;c.text(26,y-25,label,'start');c.line(X(a),y,X(b),y,'interval curve-'+str(j));c.dot(X(a),y);c.dot(X(b),y)
  for a in np.linspace(0,hi,4):c.text(X(a),241,fmt(a))
  c.text(w/2,279,'Probability' if index==17 else 'Wait (minutes)');return dict(title='Keep the interval target explicit',caption=caption,formula=formula,svg=c.finish())
 raise ValueError(f'No illustration for source {index}')

def illustration(lesson,namespace,stdout):
 code=lesson['code'];index=int(code.split('-')[0]) if code[0].isdigit() else {'sizing-and-total-cost':77,'migration-deadline-and-budget':78,'gpu-job-and-checkpoint-economics':79}[lesson['slug']]
 if index in FLOWS:
  title,steps,caption=FLOWS[index]
  return {'kind':'flow','title':title,'steps':steps,'caption':caption,'mode':'comparison' if index in (24,35,55) else 'sequence'}
 wide=image(index,640,namespace);narrow=image(index,320,namespace)
 if 'svg' not in wide:return wide
 narrow_formulas={12:r'\begin{gathered}\operatorname{median}(X)=e^\mu\\E[X]=e^{\mu+\sigma^2/2}\end{gathered}',17:r'\begin{gathered}\text{one-sided upper}\\=1-0.05^{1/n}\end{gathered}',25:r'\begin{gathered}E[A+B]=60\\\text{in both models}\end{gathered}',65:r'\begin{gathered}z=\operatorname{logsumexp}(\ell)\\\widetilde w_i=e^{\ell_i-z}\end{gathered}'}
 return {**{k:v for k,v in wide.items() if k!='svg'},'narrow_formula':narrow_formulas.get(index),'kind':'svg','wide':wide['svg'],'narrow':narrow['svg']}
