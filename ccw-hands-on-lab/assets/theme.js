(function () {
  'use strict';
  var scope = new URL('../', document.currentScript.src).href;
  var namespace = 'my-workshop:' + encodeURIComponent(scope) + ':';
  document.documentElement.dataset.workshopStorage = namespace;
  var preferred = null;
  try {
    preferred = localStorage.getItem(namespace + 'theme');
  } catch (_) {
    // Reading the course never depends on storage permissions.
  }
  var dark = preferred === 'dark' || (preferred !== 'light'
    && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
  document.documentElement.dataset.theme = dark ? 'dark' : 'light';
})();
