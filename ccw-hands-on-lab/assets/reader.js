(function () {
  'use strict';
  const root = document.documentElement;
  root.classList.add('js');
  const body = document.body;
  const $ = (selector) => document.querySelector(selector);
  const $$ = (selector) => [...document.querySelectorAll(selector)];
  const chapterLinks = $$('[data-chapter-link]');
  const chapterSlugs = chapterLinks.map((link) => link.dataset.chapterLink);
  const coreSlugs = chapterLinks.filter(link => link.dataset.coreChapter !== 'false').map(link => link.dataset.chapterLink);
  const allowedSlugs = new Set(chapterSlugs);
  const namespace = document.documentElement.dataset.workshopStorage;
  const progressKey = `${namespace}${body.dataset.courseKey}:reading:v1`;
  const themeKey = `${namespace}theme`;
  const status = $('[data-reader-status]');
  let read = new Set();
  let storageAvailable = true;
  let statusTimer;

  function announce(message) {
    clearTimeout(statusTimer);
    status.textContent = message;
    status.classList.add('is-visible');
    statusTimer = setTimeout(() => status.classList.remove('is-visible'), 4500);
  }

  function parseProgress(value) {
    try {
      const saved = JSON.parse(value);
      return new Set(saved?.version === 1 && Array.isArray(saved.read)
        ? saved.read.filter((slug) => typeof slug === 'string' && allowedSlugs.has(slug)) : []);
    } catch (_) {
      return new Set();
    }
  }

  try {
    read = parseProgress(localStorage.getItem(progressKey));
  } catch (_) {
    storageAvailable = false;
  }

  function updateProgress() {
    const count = coreSlugs.filter(slug => read.has(slug)).length;
    $$('[data-progress-count]').forEach((node) => { node.textContent = `${count} / ${coreSlugs.length} 읽음`; });
    $$('[data-reading-progress]').forEach((node) => { node.value = count; });
    chapterLinks.forEach((link) => {
      const done = read.has(link.dataset.chapterLink);
      link.classList.toggle('is-read', done);
      link.setAttribute('aria-label', `${link.querySelector('.nav-number').textContent} ${link.querySelector('.nav-title').textContent}${done ? ', 읽음' : ''}`);
    });
    const nextSlug = coreSlugs.find((slug) => !read.has(slug));
    $$('[data-route-slug]').forEach((node) => {
      node.classList.toggle('is-read', read.has(node.dataset.routeSlug));
      node.classList.toggle('is-next', node.dataset.routeSlug === nextSlug);
    });
    const current = body.dataset.currentChapter;
    const done = read.has(current);
    const toggle = $('[data-progress-toggle]');
    if (toggle) {
      toggle.setAttribute('aria-pressed', String(done));
      toggle.classList.toggle('is-read', done);
      $('[data-toggle-label]').textContent = done ? '읽음 표시 해제' : '읽음으로 표시';
      $('[data-chapter-state]').textContent = done ? '읽음' : '아직 읽지 않음';
      $('[data-chapter-state]').classList.toggle('is-read', done);
    }
    const resume = $('[data-resume-link]');
    if (resume) {
      const link = chapterLinks.find((item) => item.dataset.chapterLink === nextSlug) || chapterLinks[0];
      resume.setAttribute('href', link.getAttribute('href'));
      const number = link.querySelector('.nav-number').textContent;
      $('[data-resume-label]').textContent = !nextSlug ? '처음부터 다시 읽기'
        : count ? `이어 읽기, ${number}` : `첫 장 읽기, ${number}`;
    }
    $('[data-reset-progress]').hidden = read.size === 0;
    const note = $('[data-storage-note]');
    note.replaceChildren();
    note.append(storageAvailable ? '이 브라우저에만 저장됩니다.' : '저장할 수 없어 이 페이지에서만 표시됩니다.',
      document.createElement('br'), '실습 결과는 각 장의 확인 명령으로 점검하세요.');
  }

  function saveProgress() {
    try {
      localStorage.setItem(progressKey, JSON.stringify({
        version: 1, read: chapterSlugs.filter((slug) => read.has(slug)),
      }));
      storageAvailable = true;
    } catch (_) {
      storageAvailable = false;
    }
    updateProgress();
    revealCurrentChapter();
  }

  $('[data-progress-toggle]')?.addEventListener('click', () => {
    const slug = body.dataset.currentChapter;
    if (read.has(slug)) read.delete(slug);
    else read.add(slug);
    saveProgress();
    announce(`${read.has(slug) ? '이 장을 읽음으로 표시했습니다.' : '이 장의 읽음 표시를 해제했습니다.'}${storageAvailable ? '' : ' 이 페이지에서만 유지됩니다.'}`);
  });
  $('[data-reset-progress]').addEventListener('click', () => {
    read.clear();
    saveProgress();
    announce('이 브라우저의 읽기 기록을 초기화했습니다.');
  });
  window.addEventListener('storage', (event) => {
    if (event.key === progressKey || event.key === null) {
      read = parseProgress(event.newValue);
      updateProgress();
      revealCurrentChapter();
    }
    if (event.key === themeKey) setTheme(event.newValue === 'dark' ? 'dark' : 'light', false);
  });
  updateProgress();

  const themeToggle = $('[data-theme-toggle]');
  function setTheme(theme, persist) {
    root.dataset.theme = theme;
    const dark = theme === 'dark';
    themeToggle.setAttribute('aria-pressed', String(dark));
    themeToggle.setAttribute('aria-label', dark ? '밝은 화면으로 전환' : '어두운 화면으로 전환');
    $('[data-theme-label]').textContent = dark ? '라이트' : '다크';
    if (persist) {
      try { localStorage.setItem(themeKey, theme); } catch (_) { /* Page theme still works. */ }
    }
  }
  setTheme(root.dataset.theme === 'dark' ? 'dark' : 'light', false);
  themeToggle.addEventListener('click', () => setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark', true));
  const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
  systemTheme.addEventListener('change', (event) => {
    let saved;
    try { saved = localStorage.getItem(themeKey); } catch (_) { return; }
    if (saved !== 'light' && saved !== 'dark') setTheme(event.matches ? 'dark' : 'light', false);
  });

  const sidebar = $('#course-nav');
  const navigation = $('#chapter-navigation');
  const workspace = $('[data-workspace]');
  const backdrop = $('[data-nav-backdrop]');
  const menuToggle = $('[data-nav-toggle]');
  const mobile = window.matchMedia('(max-width: 900px)');
  const search = $('#chapter-search');
  let menuOpen = false;
  let previousFocus;

  function revealCurrentChapter() {
    if (sidebar.inert) return;
    const current = sidebar.querySelector('[aria-current="page"]');
    if (!current || current.closest('[hidden]')) return;
    const item = current.getBoundingClientRect();
    const region = navigation.getBoundingClientRect();
    if (item.bottom > region.bottom - 12) navigation.scrollTop += item.bottom - region.bottom + 12;
    else if (item.top < region.top + 12) navigation.scrollTop -= region.top + 12 - item.top;
  }

  function setMenu(open, focus = true) {
    menuOpen = mobile.matches && open;
    body.classList.toggle('nav-open', menuOpen);
    menuToggle.setAttribute('aria-expanded', String(menuOpen));
    backdrop.hidden = !menuOpen;
    sidebar.inert = mobile.matches && !menuOpen;
    workspace.inert = menuOpen;
    if (mobile.matches && !menuOpen) sidebar.setAttribute('aria-hidden', 'true');
    else sidebar.removeAttribute('aria-hidden');
    if (menuOpen) {
      sidebar.setAttribute('role', 'dialog');
      sidebar.setAttribute('aria-modal', 'true');
      if (focus) {
        previousFocus = document.activeElement;
        $('[data-nav-close]').focus();
      }
    } else {
      sidebar.removeAttribute('role');
      sidebar.removeAttribute('aria-modal');
      if (focus && previousFocus?.isConnected) previousFocus.focus({ preventScroll: true });
    }
    if (menuOpen || !mobile.matches) revealCurrentChapter();
  }
  menuToggle.addEventListener('click', () => setMenu(!menuOpen));
  $('[data-nav-close]').addEventListener('click', () => setMenu(false));
  backdrop.addEventListener('click', () => setMenu(false));
  mobile.addEventListener('change', () => setMenu(false, false));
  setMenu(false, false);
  window.addEventListener('resize', revealCurrentChapter, { passive: true });
  if (document.fonts) document.fonts.ready.then(revealCurrentChapter);

  const normalize = (value) => value.normalize('NFKC').toLocaleLowerCase('ko').replace(/\s+/g, ' ').trim();
  const navEntries = $$('[data-nav-entry]').map((node) => ({ node, terms: normalize(node.dataset.search) }));
  function filterNavigation() {
    const terms = normalize(search.value).split(' ').filter(Boolean);
    let matches = 0;
    for (const { node, terms: content } of navEntries) {
      node.hidden = !terms.every((term) => content.includes(term));
      if (!node.hidden) matches++;
    }
    $$('[data-nav-group]').forEach((group) => {
      group.hidden = ![...group.querySelectorAll('[data-nav-entry]')].some((entry) => !entry.hidden);
    });
    $('[data-search-empty]').hidden = matches !== 0;
    $('[data-search-result]').textContent = terms.length ? `${matches}개 문서가 검색되었습니다.` : '';
    if (!terms.length) revealCurrentChapter();
  }
  search.addEventListener('input', filterNavigation);
  search.addEventListener('search', filterNavigation);
  document.addEventListener('keydown', (event) => {
    const editing = event.target instanceof Element && event.target.closest('input, textarea, select, [contenteditable="true"]');
    if (event.key === '/' && !editing && !event.ctrlKey && !event.metaKey && !event.altKey) {
      event.preventDefault();
      if (mobile.matches) setMenu(true);
      search.focus();
    }
    if (event.key === 'Escape') {
      if (document.activeElement === search && search.value) {
        search.value = '';
        filterNavigation();
      } else if (menuOpen) setMenu(false);
    }
    if (event.key === 'Tab' && menuOpen) {
      const focusable = [...sidebar.querySelectorAll('a[href], button, input, [tabindex="0"]')]
        .filter((node) => !node.disabled && node.getClientRects().length);
      const first = focusable[0];
      const last = focusable.at(-1);
      if (event.shiftKey && (document.activeElement === first || !sidebar.contains(document.activeElement))) {
        event.preventDefault();
        last?.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first?.focus();
      }
    }
  });

  function fallbackCopy(value) {
    const textarea = document.createElement('textarea');
    textarea.className = 'copy-fallback';
    textarea.value = value;
    textarea.readOnly = true;
    textarea.setAttribute('aria-label', '복사할 코드');
    document.body.append(textarea);
    textarea.select();
    let copied = false;
    try { copied = document.execCommand('copy'); } catch (_) { /* Selection is offered below. */ }
    textarea.remove();
    return copied;
  }

  const promptScreens = $$('[data-prompt-screen]');
  const promptApps = { codex: 'Codex', kiro: 'Kiro CLI', claude: 'Claude Code' };
  const promptPreferenceKey = `${namespace}prompt-app`;
  function choosePromptApp(value, persist = false) {
    const selected = Object.hasOwn(promptApps, value) ? value : 'codex';
    promptScreens.forEach(screen => {
      screen.dataset.assistant = selected;
      screen.querySelector('[data-prompt-app]').textContent = promptApps[selected];
      screen.querySelector('[data-prompt-destination]').textContent =
        `${promptApps[selected]}의 대화 입력창에 붙여넣으세요.`;
      screen.querySelectorAll('[data-prompt-tool]').forEach(button =>
        button.setAttribute('aria-pressed', String(button.dataset.promptTool === selected)));
      const copy = screen.querySelector('[data-copy-code]');
      copy.dataset.copyLabel = `${promptApps[selected]} 프롬프트 복사`;
      copy.setAttribute('aria-label', copy.dataset.copyLabel);
    });
    if (persist) {
      try { localStorage.setItem(promptPreferenceKey, selected); } catch (_) { /* This page still keeps the choice. */ }
    }
  }
  let promptApp = 'codex';
  try { promptApp = localStorage.getItem(promptPreferenceKey) || promptApp; } catch (_) { /* Default is available offline. */ }
  choosePromptApp(promptApp);
  $$('[data-prompt-tool]').forEach(button =>
    button.addEventListener('click', () => choosePromptApp(button.dataset.promptTool, true)));

  $$('[data-copy-code]').forEach((button) => {
    button.addEventListener('click', async () => {
      const code = document.getElementById(button.dataset.copyCode);
      if (!code) return;
      const originalLabel = button.getAttribute('aria-label');
      const isPrompt = Boolean(button.closest('[data-prompt-screen]'));
      let copied = false;
      button.disabled = true;
      try {
        if (navigator.clipboard?.writeText) {
          await navigator.clipboard.writeText(code.textContent);
          copied = true;
        }
      } catch (_) { /* file:// and blocked clipboard permissions use selection copy. */ }
      if (!copied) copied = fallbackCopy(code.textContent);
      button.disabled = false;
      button.focus({ preventScroll: true });
      if (!copied) {
        const range = document.createRange();
        range.selectNodeContents(code);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
      }
      button.textContent = copied ? '복사됨' : '선택됨';
      button.setAttribute('aria-label', copied ? isPrompt ? '프롬프트를 복사했습니다' : '코드를 복사했습니다' : '선택한 내용을 직접 복사하세요');
      announce(copied ? isPrompt ? '프롬프트를 복사했습니다.' : '코드를 복사했습니다.' : '내용을 선택했습니다. Ctrl+C 또는 ⌘C로 복사하세요.');
      setTimeout(() => { button.textContent = '복사'; button.setAttribute('aria-label', button.dataset.copyLabel || originalLabel); }, 2200);
    });
  });

  const toc = $('[data-page-toc]');
  if (toc && window.matchMedia('(max-width: 1250px)').matches) toc.open = false;
  const tocLinks = $$('[data-toc-link]');
  if ('IntersectionObserver' in window && tocLinks.length) {
    const byId = new Map(tocLinks.map((link) => [decodeURIComponent(link.hash.slice(1)), link]));
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
      if (!visible.length) return;
      const active = byId.get(visible[0].target.id);
      tocLinks.forEach((link) => {
        link.classList.toggle('is-active', link === active);
        if (link === active) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }, { rootMargin: '-90px 0px -60% 0px', threshold: 0 });
    byId.forEach((_, id) => { const heading = document.getElementById(id); if (heading) observer.observe(heading); });
  }

  $('[data-print]').addEventListener('click', () => window.print());
  let printDetails = [];
  window.addEventListener('beforeprint', () => {
    printDetails = $$('main details').map((details) => [details, details.open]);
    printDetails.forEach(([details]) => { details.open = true; });
  });
  window.addEventListener('afterprint', () => {
    printDetails.forEach(([details, open]) => { details.open = open; });
  });
})();
