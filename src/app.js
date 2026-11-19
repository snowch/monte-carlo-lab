import katex from './vendor/katex.mjs';
import {renderRich} from './rich-text.mjs';
// Copyright © 2026 Christopher Snow
import {attachEditor} from './editor.mjs';

// Prepare after the first paint, only on visible runnable lessons.
function schedulePreparation(start){
 const connection=navigator.connection;
 if(connection?.saveData||/^(slow-)?[23]g$/.test(connection?.effectiveType||'')||
    (connection?.downlink>0&&connection.downlink<1.5)||navigator.deviceMemory<=2)return ()=>{};
 let cancelled=false,scheduled=false,frame,task;
 const useIdle=typeof requestIdleCallback==='function';
 function cancel(){
  cancelled=true;
  document.removeEventListener('visibilitychange',schedule);
  cancelAnimationFrame(frame);
  if(useIdle)cancelIdleCallback(task);else clearTimeout(task);
 }
 function schedule(){
  if(cancelled||scheduled||document.visibilityState!=='visible')return;
  scheduled=true;
  frame=requestAnimationFrame(()=>{
   frame=requestAnimationFrame(()=>{
    const prepare=()=>{
     scheduled=false;
     if(cancelled||document.visibilityState!=='visible')return;
     cancel();
     start();
    };
    task=useIdle?requestIdleCallback(prepare,{timeout:2000}):setTimeout(prepare,500);
   });
  });
 }
 document.addEventListener('visibilitychange',schedule);
 schedule();
 return cancel;
}
const root=new URL('.',import.meta.url);
const $=id=>document.getElementById(id);
const prefix='mcl:v1:';
let storageAvailable=true;
function get(key,fallback=''){
 try{return localStorage.getItem(prefix+key)??fallback}catch{storageAvailable=false;return fallback}
}
function put(key,value){
 try{localStorage.setItem(prefix+key,String(value));return true}catch{return false}
}
function storageMessage(message){
 const target=$('storage-error');
 target.textContent=message;target.hidden=!message;
}
function download(name,body,type='application/json'){
 const url=URL.createObjectURL(new Blob([body],{type}));
 const anchor=document.createElement('a');anchor.href=url;anchor.download=name;anchor.click();
 setTimeout(()=>URL.revokeObjectURL(url),1000);
}
function updateReadMarks(){
 document.querySelectorAll('[data-read]').forEach(el=>el.textContent=get('read:'+el.dataset.read)==='true'?'✓ Read':'');
}
$('theme')?.addEventListener('click',()=>{
 const theme=document.documentElement.dataset.theme==='dark'?'light':'dark';
 document.documentElement.dataset.theme=theme;
 try{localStorage.setItem('mcl:theme',theme)}catch{}
 setThemeLabel();
});
function setThemeLabel(){const dark=document.documentElement.dataset.theme==='dark';$('theme')?.setAttribute('aria-label',`Switch to ${dark?'light':'dark'} theme`)}
setThemeLabel();
const menu=$('course-menu-toggle'),sidebar=$('course-sidebar');
if(menu&&sidebar){
 const close=()=>{sidebar.classList.remove('is-open');menu.setAttribute('aria-expanded','false')};
 menu.addEventListener('click',()=>{const open=sidebar.classList.toggle('is-open');menu.setAttribute('aria-expanded',String(open))});
 document.addEventListener('keydown',event=>{if(event.key==='Escape'&&sidebar.classList.contains('is-open')){close();menu.focus()}});
 matchMedia('(min-width: 961px)').addEventListener('change',event=>{if(event.matches)close()});
}
const course=await fetch(new URL('course.json',root),{cache:'no-cache'}).then(response=>{if(!response.ok)throw new Error('Course data could not load. Please reload.');return response.json()}).catch(error=>{
 const target=$('status')||$('progress-status');if(target)target.textContent=error.message;return null;
});
if(course){
 updateReadMarks();
 if($('search'))initializeOverview(course);
 const lesson=[course.introduction,...course.lessons,...course.applications].find(l=>l.slug===document.querySelector('[data-slug]')?.dataset.slug);
 if(lesson)initializeLesson(lesson);
 document.documentElement.dataset.ready='true';
}
function initializeOverview({lessons,applications,introduction}){
 function progress(){
  const read=lessons.filter(l=>get('read:'+l.slug)==='true').length;
  $('progress-count').textContent=`${read} / ${lessons.length} read`;
  $('course-progress').value=read;
  const next=lessons.find(l=>get('read:'+l.slug)!=='true');
  $('start-course').href=next?'lessons/'+next.slug+'.html':'#course';
  $('start-label').textContent=next?(read?'Continue learning':'Start lesson 1'):'Review course contents';
  updateReadMarks();
 }
 progress();
 if(!storageAvailable)$('progress-status').textContent='This browser could not open saved progress.';
 const modules=[...document.querySelectorAll('.module')];
 const savedOpen=new Map();let searching=false;
 const revealModule=()=>{const module=document.getElementById(location.hash.slice(1));if(module?.classList.contains('module'))module.open=true};
 revealModule();window.addEventListener('hashchange',revealModule);
 $('search').addEventListener('input',()=>{
  const words=$('search').value.toLowerCase().trim().split(/\s+/).filter(Boolean);
  if(words.length&&!searching){for(const module of modules)savedOpen.set(module,module.open);searching=true}
  let count=0;
  document.querySelectorAll('.lesson-row').forEach(row=>{const match=words.every(word=>row.dataset.search.includes(word));row.hidden=!match;if(match)count++});
  for(const module of modules){
   module.hidden=![...module.querySelectorAll('.lesson-row')].some(row=>!row.hidden);
   if(words.length)module.open=!module.hidden;
   else if(searching)module.open=savedOpen.get(module)??false;
  }
  if(!words.length){searching=false;savedOpen.clear()}
  $('search-count').textContent=`${count} investigation${count===1?'':'s'}`;
  $('search-empty').hidden=count!==0;
 });
 $('export-progress').addEventListener('click',()=>{
  const data={};
  try{
   for(let i=0;i<localStorage.length;i++){
    const key=localStorage.key(i);
    if(key?.startsWith(prefix))data[key.slice(prefix.length)]=localStorage.getItem(key);
   }
  }catch{
   $('progress-status').textContent='This browser could not read saved progress. No file was downloaded.';
   return;
  }
  download('monte-carlo-lab-progress.json',JSON.stringify({course:'monte-carlo-lab',schema:1,exported_at:new Date().toISOString(),data},null,2));
  $('progress-status').textContent='Exported saved reading marks, attempts and drafts. Run results and CSV inputs require their own exports.';
 });
 $('import-progress').addEventListener('change',async()=>{
  const file=$('import-progress').files[0];if(!file)return;
  try{
   if(file.size>1_000_000)throw new Error('Progress file must be smaller than 1 MB.');
   const record=JSON.parse(await file.text());
   if(record.course!=='monte-carlo-lab'||record.schema!==1||!record.data||typeof record.data!=='object'||Array.isArray(record.data))throw new Error('Not a version 1 Monte Carlo Lab progress file.');
   const slugs=new Set([introduction,...lessons,...applications].map(l=>l.slug));
   const fields=new Set(['code','restore-backup','prediction','notes','quiz','report-question','report-plan','report-source','report-finding','report-limits']);
   const entries=Object.entries(record.data);
   for(const[key,value]of entries){
    const [type,slug,field,...extra]=key.split(':');
    if(extra.length||!slugs.has(slug)||typeof value!=='string'||value.length>300_000||!((type==='read'&&!field&&(value==='true'||value==='false'))||(type==='draft'&&fields.has(field))))throw new Error('Progress file contains an invalid record. Nothing has been imported.');
   }
   let saved=0;for(const[key,value]of entries)if(put(key,value))saved++;
   progress();$('progress-status').textContent=saved===entries.length?`Imported ${saved} saved records. Matching records in this browser were replaced.`:`Saved ${saved} of ${entries.length} records. Keep the import file and check browser storage before retrying.`;
  }catch(error){$('progress-status').textContent=error.message}
  $('import-progress').value='';
 });
}
const rich=text=>renderRich(text,tex=>katex.renderToString(tex,{displayMode:false,throwOnError:false,trust:false,strict:'warn'}));
function initializeLesson(lesson){
 const slug=lesson.slug;
 const initialCode=$('code').value;
 let worker=null,timer=null,busy=false,readingCsv=false,lastSuccessfulRun=null,csv=null,csvName=null,revision=0;
 let plotUrls=[];
 function clearPlots(){for(const url of plotUrls)URL.revokeObjectURL(url);plotUrls=[];$('plots').replaceChildren()}
 function svgUrl(base64){const bytes=Uint8Array.from(atob(base64),c=>c.charCodeAt(0));const url=URL.createObjectURL(new Blob([bytes],{type:'image/svg+xml'}));plotUrls.push(url);return url}
 const initialQuiz=get(`draft:${slug}:quiz`);
 const draftKey=id=>`draft:${slug}:${id}`;
 $('code').value=get(draftKey('code'),initialCode);
 let recoverableDraft=get(draftKey('restore-backup'),null);
 $('saved-draft-note').hidden=$('code').value===initialCode;
 const refreshEditor=attachEditor($('code'));
 const unsavedReportFields=new Set();
 function updatePreparation(){
  document.querySelector('.prepared-state').hidden=$('code').value!==initialCode||csv!==null;
 }
 updatePreparation();
 function saveField(el){
  const saved=put(draftKey(el.dataset.save),el.value);
  if(el.id==='notes'){
   $('save-note').textContent=saved?'Notes saved in this browser.':'The browser could not save these edits. Copy the open notes before leaving. Reloading may show older notes.';
  }else if(el.id.startsWith('report-')){
   if(saved)unsavedReportFields.delete(el.id);
   else unsavedReportFields.add(el.id);
   $('report-draft-status').textContent=unsavedReportFields.size
    ?'The browser could not save some report edits. Export the investigation to keep the text currently open.'
    :'Report fields saved in this browser.';
  }else{
   $('prediction-status').textContent=saved?'':'This browser could not save your prediction. Copy it before leaving to keep the current text.';
  }
 }
 document.querySelectorAll('[data-save]').forEach(el=>{
  el.value=get(draftKey(el.dataset.save));
  if(el.value&&el.closest('details')&&el.id!=='code')el.closest('details').open=true;
  el.addEventListener('input',()=>saveField(el));
 });
 $('mark-read').checked=get('read:'+slug)==='true';
 if(!storageAvailable)storageMessage('This browser could not open your saved work. Python can still run. To keep edits, copy them or export a record before leaving.');
 $('mark-read').addEventListener('change',()=>{
  const saved=put('read:'+slug,$('mark-read').checked);
  if(!saved)$('mark-read').checked=get('read:'+slug)==='true';
  $('read-status').textContent=saved?'':'This browser could not save the reading mark.';
  updateReadMarks();
 });
 function stale(){
  if(!lastSuccessfulRun)return;
  const changed=$('code').value!==lastSuccessfulRun.source || csv!==lastSuccessfulRun.input_csv || csvName!==lastSuccessfulRun.input_name;
  const message=busy?'A new run is in progress. This result is from the last successful run.':changed
   ?'Code or input changed. This result and its export use the last successful run.'
   :`Last successful run at ${new Date(lastSuccessfulRun.executed_at).toLocaleTimeString()}.`;
  const input=$('csv-upload')?` CSV for this result · ${lastSuccessfulRun.input_name||'none supplied'}.`:'';
  $('output-provenance').textContent=message+input;
  $('output-provenance').classList.toggle('stale',changed||busy);
 }
 function updateRecovery(){
  $('recover-draft').hidden=recoverableDraft===null||recoverableDraft===$('code').value;
 }
 function showCode(code){
  const current=$('code').value;
  // Save the outgoing draft before replacing its persisted copy.
  let canSave=true;
  if(current!==initialCode&&current!==code){
   recoverableDraft=current;
   canSave=put(draftKey('restore-backup'),current);
  }
  $('code').value=code;
  refreshEditor();
  const saved=canSave&&put(draftKey('code'),code);
  storageMessage(saved?'':'This browser could not save the open code. Use Tools → Download Python to keep a copy.');
  $('saved-draft-note').hidden=true;
  updatePreparation();
  updateRecovery();
  stale();
  $('editor-tools').open=false;
  $('code').focus();
  return saved;
 }
 updateRecovery();
 $('code').addEventListener('input',()=>{
  const saved=put(draftKey('code'),$('code').value);
  storageMessage(saved?'':'This browser could not save the open code. Use Tools → Download Python to keep a copy.');
  $('saved-draft-note').hidden=true;
  updatePreparation();
  updateRecovery();
  stale();
 });
 $('code').addEventListener('keydown',event=>{
  if((event.ctrlKey||event.metaKey)&&event.key==='Enter'){event.preventDefault();if(!busy)run()}
 });
 $('restore').addEventListener('click',()=>{
  const saved=showCode(initialCode);
  $('status').textContent=recoverableDraft===null
   ?'Published code is ready. Select Run Python.'
   :saved?'Published code is ready. To get your draft back, use Recover draft in Tools.'
    :'Published code is ready. To get your draft back in this tab, use Recover draft in Tools before reloading.';
 });
 $('recover-draft').addEventListener('click',()=>{
  if(recoverableDraft===null)return;
  showCode(recoverableDraft);
  $('status').textContent='Draft recovered. Select Run Python to run this code.';
 });
 $('download-code').addEventListener('click',()=>download(slug+'.py',$('code').value,'text/x-python'));
 $('back-to-editor').addEventListener('click',event=>{
  event.preventDefault();
  $('code').focus({preventScroll:true});
  $('code-editor').scrollIntoView({block:'start'});
 });
 $('export-run').addEventListener('click',()=>{
  if(!lastSuccessfulRun)return;
  const notes={prediction:$('prediction').value,notes:$('notes').value};
  download(slug+'-run.json',JSON.stringify({...lastSuccessfulRun,notes},null,2));
 });
 function controls(running){
  const returnFocus=!running&&document.activeElement===$('stop');
  busy=running;document.querySelector('.experiment').classList.toggle('is-running',running);$('code-editor').setAttribute('aria-busy',String(running));$('run').disabled=running||readingCsv;$('stop').disabled=!running;$('stop').hidden=!running;$('restore').disabled=running;
  $('recover-draft').disabled=running;
  if($('csv-upload'))$('csv-upload').disabled=running||readingCsv;
  if($('clear-csv')){
   $('clear-csv').hidden=csv===null;
   $('clear-csv').disabled=running||readingCsv||csv===null;
  }
  if(returnFocus)$('run').focus({preventScroll:true});
 }
 let pythonPrepared=false, preparationTimer;
 function disposePython(){
  clearTimeout(preparationTimer);
  worker?.terminate();
  worker=null;
  pythonPrepared=false;
 }
 function pythonWorker(){
  return worker ??= new Worker(new URL('worker.js',root));
 }
 function preparePython(){
  if(worker||busy)return;
  try{
   const preparing=pythonWorker();
   const abandon=()=>{if(worker===preparing&&!busy)disposePython()};
   preparing.onerror=abandon;
   preparing.onmessage=({data})=>{
    if(data.type==='prepare-error'){abandon();return}
    if(data.type==='prepared'){
     clearTimeout(preparationTimer);
     pythonPrepared=true;
    }
   };
   preparationTimer=setTimeout(abandon,120000);
   preparing.postMessage({type:'prepare'});
  }catch{disposePython()}
 }
 const cancelPreparation=schedulePreparation(preparePython);
 function terminate(message){
  revision++;clearTimeout(timer);disposePython();controls(false);$('status').textContent=message;
  stale();
 }
 function showRunError(message,inputName,stdout=''){
  const traceback=message.trim();
  const details=[stdout.trimEnd(),traceback].filter(Boolean).join('\n\n');
  $('error-summary').textContent=traceback.split('\n').at(-1)||'Python could not finish.';
  $('error-input').hidden=inputName===null;
  $('error-input').textContent=inputName===null?'':`CSV for this attempt · ${inputName}.`;
  $('error-trace').textContent=details;
  $('error-details').hidden=!details.includes('\n');
  $('run-error').hidden=false;
  stale();
 }
 $('stop').addEventListener('click',()=>terminate('Stopped. No result was saved for the cancelled run. Run again to restart Python.'));
 $('restart-python').addEventListener('click',()=>{
  cancelPreparation();
  terminate('Python session reset. Select Run Python to start again.');
 });
 async function run(){
  if(busy||readingCsv)return;
  cancelPreparation();
  clearTimeout(preparationTimer);
  const source=$('code').value,input=csv,inputName=csvName,runRevision=++revision;
  const runWasFocused=document.activeElement===$('run');
  $('editor-tools').open=false;
  $('run-error').hidden=true;
  $('error-details').open=false;
  controls(true);
  if(runWasFocused)$('stop').focus({preventScroll:true});
  $('status').textContent=pythonPrepared?'Starting your Python…':'Loading Python and statistics packages. This can take a moment…';
  stale();
  const fail=message=>{
   if(runRevision!==revision)return;
   terminate('Python could not finish. Check the message, then edit or run again.');
   showRunError(message,inputName);
  };
  timer=setTimeout(()=>fail('Python initialization exceeded two minutes. Check your connection and run again.'),120000);
  try{pythonWorker()}catch(error){fail(error.message);return}
  worker.onerror=event=>fail(event.message||'The Python worker could not load.');
  worker.onmessage=({data})=>{
   if(runRevision!==revision)return;
   if(data.type==='running'){
    pythonPrepared=true;
    clearTimeout(timer);$('status').textContent='Running your Python…';
    timer=setTimeout(()=>fail('Execution exceeded 45 seconds and was stopped. Reduce the work or fix a loop, then run again.'),45000);return;
   }
   if(data.type==='error'){fail(data.message);return}
   if(data.type!=='result')return;
   clearTimeout(timer);controls(false);
   const {stdout,error,figures,figures_narrow=[],versions}=data.value;
   if(error){
    $('status').textContent=inputName===null
     ?'Python reported an error. Check the message, then edit the code and run again.'
     :'Python reported an error. Check the message, then fix the CSV or code and run again. Open Use your own CSV to select a different file.';
    showRunError(error,inputName,stdout);
    return;
   }
   $('run-result').hidden=false;
   lastSuccessfulRun={schema:1,course:'monte-carlo-lab',lesson:slug,executed_at:new Date().toISOString(),source,input_csv:input,input_name:inputName,stdout,error:null,figures_svg_base64:figures,figures_narrow_svg_base64:figures_narrow,versions,environment:{user_agent:navigator.userAgent,timing_scope:'Local browser Pyodide; see executed source for boundaries.'}};
   $('output').textContent=stdout||'No text was printed.';
   clearPlots();
   $('plots').replaceChildren(...figures.map((svg,i)=>{
    const figure=document.createElement('figure');figure.className='worked-figure';
    const picture=document.createElement('picture');
    const image=document.createElement('img');image.className='plot';image.src=svgUrl(svg);image.alt=`Plot ${i+1} from your actual Python execution. Read its labelled axes and the text output together.`;
    if(figures_narrow[i]){const source=document.createElement('source');source.media='(max-width:700px)';source.srcset=svgUrl(figures_narrow[i]);picture.append(source)}
    picture.append(image);const caption=document.createElement('figcaption'),link=document.createElement('a');
    link.href=image.src;link.target='_blank';link.rel='noopener';link.textContent='Open full-size figure ↗';caption.append(link);figure.append(picture,caption);return figure;
   }));
   $('status').textContent='Completed. Your result is below.';
   $('export-run').disabled=false;$('export-run').hidden=false;stale();
  };
  worker.postMessage({type:'run',source,csv:input});
 }
 $('run').addEventListener('click',run);
 window.addEventListener('pagehide',event=>{
  cancelPreparation();
  revision++;
  clearTimeout(timer);
  disposePython();
  if(busy){
   controls(false);
   $('status').textContent='Select Run Python to start again.';
   stale();
  }
  if(!event.persisted)clearPlots();
 });
 let quizAttempt=null;
 try{quizAttempt=JSON.parse(initialQuiz)}catch{}
 if(quizAttempt&&Number.isInteger(quizAttempt.answer)&&quizAttempt.answer>=0&&quizAttempt.answer<lesson.options.length){
  const choice=document.querySelector(`input[name=answer][value="${quizAttempt.answer}"]`);if(choice)choice.checked=true;
 }
 $('quiz').addEventListener('submit',event=>{
  event.preventDefault();const selected=document.querySelector('input[name=answer]:checked');
  if(!selected){$('quiz-feedback').textContent='Choose an answer first, then check your reasoning.';return}
  const answer=Number(selected.value),correct=answer===lesson.correct;
  const saved=put(draftKey('quiz'),JSON.stringify({answer,correct,at:new Date().toISOString()}));
  const feedback=$('quiz-feedback');feedback.replaceChildren();feedback.classList.toggle('incorrect',!correct);
  const title=document.createElement('b');title.textContent=correct?'That reasoning fits.':'Reconsider the comparison.';
  const text=document.createElement('span');text.innerHTML=rich(lesson.feedback);
  feedback.append(title,text);
  if(!saved)feedback.append(document.createTextNode(' This browser could not save your answer.'));
  feedback.focus({preventScroll:true});
 });
 if($('csv-upload')){
  function showInput(){
   $('input-kind').textContent=csvName===null?'Next run uses invented starter data':`CSV for next run · ${csvName}`;
   updatePreparation();
  }
  $('csv-upload').addEventListener('change',async()=>{
   const picker=$('csv-upload');
   const file=picker.files[0];if(!file)return;
   const pickerHadFocus=document.activeElement===picker;
   readingCsv=true;
   controls(false);
   $('csv-status').textContent=`Reading ${file.name}…`;
   try{
    if(file.size>1_000_000)throw new Error('CSV must be 1 MB or smaller.');
    const bytes=await file.arrayBuffer();
    let text;
    try{text=new TextDecoder('utf-8',{fatal:true,ignoreBOM:true}).decode(bytes)}catch{throw new Error('Save the CSV as UTF-8 and choose it again.');}
    if(!text.trim())throw new Error('The file is empty.');
    csv=text;csvName=file.name;
    $('csv-status').textContent='File ready. Select Run Python to check and analyse it.';
    showInput();
    stale();
   }catch(error){$('csv-status').textContent=`${file.name} · ${error.message} The previous input is unchanged.`}
   finally{
    readingCsv=false;
    picker.value='';
    controls(false);
    if(pickerHadFocus&&document.activeElement===document.body)picker.focus({preventScroll:true});
   }
  });
  $('clear-csv').addEventListener('click',()=>{
   csv=null;
   csvName=null;
   $('csv-status').textContent='Invented starter data selected.';
   showInput();
   controls(false);
   stale();
   $('csv-upload').focus();
  });
  $('export-report').addEventListener('click',()=>{
   function codeBlock(language,text){
    const longest=(text.match(/`+/g)||[]).reduce((length,run)=>Math.max(length,run.length),2);
    const fence='`'.repeat(longest+1);
    return `${fence}${language}\n${text}\n${fence}`;
   }
   const fields=[['question','Question & useful threshold'],['plan','Model & analysis plan'],['source','Data source & conditions'],['finding','Finding & uncertainty'],['limits','Limitations & next test']];
   const body=['# Monte Carlo Lab · Investigation',`Exported ${new Date().toISOString()}`];
   for(const[id,label]of fields)body.push(`## ${label}\n\n${$('report-'+id).value||'[Not recorded]'}`);
   body.push('## Execution record');
   if(lastSuccessfulRun){
    const {executed_at,input_name,versions,source,stdout,input_csv}=lastSuccessfulRun;
    body.push(`Last successful run at ${executed_at}. Input: ${input_name||'Inspect the source for starter data.'}\n\nVersions: ${JSON.stringify(versions)}`);
    body.push('### Exact executed Python\n\n'+codeBlock('python',source));
    body.push('### Actual output\n\n'+codeBlock('text',stdout));
    if(input_csv!==null)body.push('### Exact input CSV\n\n'+codeBlock('csv',input_csv));
    if($('code').value!==source||csv!==input_csv||csvName!==input_name)body.push('The editor or selected input changed after this run. The record above preserves the last successful execution.');
   }else body.push('No successful execution was recorded on this page. Worked output is available separately in the lesson.');
   body.push('## Field notes\n\n'+($('notes').value||'[Not recorded]'));
   download('monte-carlo-investigation.md',body.join('\n\n')+'\n','text/markdown');
   $('report-status').textContent='Investigation exported. Save your original data and run JSON alongside it.';
  });
 }
 controls(false);
}

document.addEventListener('click',event=>{
 for(const details of document.querySelectorAll('.header-help[open],.editor-tools[open]'))if(!details.contains(event.target))details.open=false;
});
document.addEventListener('keydown',event=>{
 if(event.key!=='Escape')return;
 const open=[...document.querySelectorAll('.header-help[open],.editor-tools[open]')];
 const target=open.find(d=>d.contains(document.activeElement))||open.at(-1);
 if(target){target.open=false;target.querySelector('summary').focus()}
});
