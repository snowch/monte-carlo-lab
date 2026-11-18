"""Regression checks for the quieter default UI and the tablet layout reported by the user."""
def check_quiet_layout(browser,root,base,lessons):
    context=browser.new_context(viewport={'width':820,'height':1180},reduced_motion='reduce')
    page=context.new_page()
    cases=[lessons[0],lessons[len(lessons)//2],next((l for l in lessons if l.get('capstone')),lessons[-1])]
    def visit(path):
        page.goto(base+path);page.wait_for_selector('html[data-ready=true]')
    for width in [820,1024]:
        page.set_viewport_size({'width':width,'height':1180})
        for i,lesson in enumerate(cases):
            visit('lessons/'+lesson['slug']+'.html')
            assert page.locator('.outcome,.on-this-page,.mobile-course-bar,.result-hint,.execution-status').count()==0
            assert page.locator('.standfirst').inner_text()==lesson['goal']
            assert not page.locator('#run-result').is_visible()
            assert not page.locator('#stop').is_visible()
            assert not page.locator('#export-run').is_visible()
            assert not page.locator('#prediction').is_visible()
            assert not page.locator('#notes').is_visible()
            assert not page.locator('#restore').is_visible()
            assert page.locator('.data-kind').inner_text().strip()
            assert page.locator('.prepared-state').is_visible()
            assert page.locator('.prepared-state').inner_text().startswith('Select Run Python')
            assert page.locator('button.primary:visible').count()==1
            page.locator('#back-to-editor').press('Enter')
            assert page.evaluate('document.activeElement.id')=='code'
            assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),(width,lesson['slug'])
            assert page.locator('.explanation p').first.evaluate('e=>parseFloat(getComputedStyle(e).fontSize)')>=20
            if width==820 and i==0:
                top=page.locator('.explanation p').first.evaluate('e=>e.getBoundingClientRect().top')
                assert top<460,('tablet introduction still delayed',top)
                assert page.locator('.site-header').evaluate('e=>e.getBoundingClientRect().height')<=85
                page.screenshot(path=str(root/'test-results/quiet-tablet.png'))
            tools=page.locator('#editor-tools')
            tools.locator(':scope > summary').click();assert page.locator('#restore').is_visible()
            page.keyboard.press('Escape');assert not tools.evaluate('e=>e.open')
            assert page.evaluate('document.activeElement.textContent')=='Tools'
            if width==820:
                page.locator('#course-menu-toggle').click();assert page.locator('#course-sidebar').is_visible()
                page.keyboard.press('Escape');assert not page.locator('#course-sidebar').is_visible()
            else:
                assert page.locator('#course-sidebar').is_visible()
                assert not page.locator('#course-menu-toggle').is_visible()
        visit('')
        assert page.locator('.course-hero .hero-illustration').is_visible()
        assert page.locator('.course-art title').text_content().strip()
        assert page.locator('.course-hero #start-course').is_visible()
        assert page.locator('.module[open]').count()==1
        assert page.locator('.method-strip,.route-guide,.progress-panel,.closing').count()==0
        middle=lessons[len(lessons)//2]
        page.locator('#search').fill(middle['title'])
        assert page.locator(f'.lesson-row[href="lessons/{middle["slug"]}.html"]').is_visible()
        page.locator('#search').fill('')
        assert page.locator('.module[open]').count()==1
        visit('index.html#module-'+str(middle['module']+1))
        assert page.locator('#module-'+str(middle['module']+1)).evaluate('e=>e.open')
        page.locator('.header-help > summary').click()
        assert page.locator('.header-help a',has_text='Source on GitHub').is_visible()
        page.keyboard.press('Escape');assert not page.locator('.header-help').evaluate('e=>e.open')
    context.close()
    blocked=browser.new_context(viewport={'width':820,'height':1180},reduced_motion='reduce')
    blocked.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw new Error('storage blocked for test')}})")
    reader=blocked.new_page();reader.goto(base+'lessons/'+lessons[0]['slug']+'.html')
    reader.wait_for_selector('html[data-ready=true]')
    assert reader.locator('#storage-error').is_visible()
    assert 'could not open your saved work' in reader.locator('#storage-error').inner_text()
    assert reader.locator('#run').is_enabled()
    reader.goto(base);reader.wait_for_selector('html[data-ready=true]')
    reader.locator('.portable-progress summary').click()
    reader.locator('#export-progress').click()
    assert 'No file was downloaded' in reader.locator('#progress-status').inner_text()
    blocked.close()
    writing=browser.new_context(viewport={'width':390,'height':844})
    editor=writing.new_page()
    editor.goto(base+'lessons/'+lessons[0]['slug']+'.html')
    editor.wait_for_selector('html[data-ready=true]')
    editor.locator('#lesson-notes summary').press('Enter')
    assert editor.locator('#save-note').text_content()==''
    editor.locator('#notes').fill('Earlier saved note')
    assert 'Notes saved' in editor.locator('#save-note').inner_text()
    editor.evaluate("""() => {
        const original = Storage.prototype.setItem;
        Storage.prototype.setItem = function(key, value) {
            if (key.startsWith('mcl:v1:') && window.rejectDraftWrites) {
                throw new DOMException('Full', 'QuotaExceededError');
            }
            return original.call(this, key, value);
        };
        window.rejectDraftWrites = true;
    }""")
    editor.locator('#notes').fill('Current unsaved note')
    assert 'could not save these edits' in editor.locator('#save-note').inner_text()
    assert editor.locator('#notes').input_value()=='Current unsaved note'
    editor.locator('#code').fill('print(123)')
    assert 'could not save the open code' in editor.locator('#storage-error').inner_text()
    editor.evaluate('window.rejectDraftWrites = false')
    editor.locator('#code').fill('print(456)')
    assert not editor.locator('#storage-error').is_visible()
    editor.reload()
    editor.wait_for_selector('html[data-ready=true]')
    assert editor.locator('#notes').input_value()=='Earlier saved note'
    assert editor.locator('#code').input_value()=='print(456)'
    capstone=next(lesson for lesson in lessons if lesson['capstone'])
    editor.goto(base+'lessons/'+capstone['slug']+'.html')
    editor.wait_for_selector('html[data-ready=true]')
    editor.locator('#report-question').fill('Earlier saved question')
    editor.evaluate("""() => {
        const original = Storage.prototype.setItem;
        Storage.prototype.setItem = function(key, value) {
            if (key.endsWith(':report-question')) {
                throw new DOMException('Full', 'QuotaExceededError');
            }
            return original.call(this, key, value);
        };
    }""")
    editor.locator('#report-question').fill('Current open question')
    editor.locator('#report-source').fill('Saved source entry')
    assert 'could not save some report edits' in editor.locator('#report-draft-status').inner_text()
    with editor.expect_download() as export:
        editor.locator('#export-report').press('Enter')
    assert 'Current open question' in export.value.path().read_text()
    assert 'could not save some report edits' in editor.locator('#report-draft-status').inner_text()
    editor.reload()
    editor.wait_for_selector('html[data-ready=true]')
    assert editor.locator('#report-question').input_value()=='Earlier saved question'
    assert editor.locator('#report-source').input_value()=='Saved source entry'
    writing.close()
    print('PASS quiet default states, 820/1024px tablet/sidebar layouts, optional tools, module search and deep links.',flush=True)
