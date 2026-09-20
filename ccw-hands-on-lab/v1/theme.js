// Dark/light theme toggle, shared across ccw-hands-on-lab pages.
// Runs before first paint (blocking <head> script) to avoid a flash of the wrong theme.
(function () {
  var KEY = "ccw-theme";
  var stored = null;
  try { stored = localStorage.getItem(KEY); } catch (e) {}
  var theme = stored || (matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
  document.documentElement.dataset.theme = theme;

  // Inline SVG, not unicode glyphs — ☀/☾ render as tofu in the page's Korean webfont.
  var SUN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"'
    + ' stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/>'
    + '<path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2'
    + 'M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M18.7 5.3l-1.6 1.6M6.9 17.1l-1.6 1.6"/></svg>';
  var MOON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"'
    + ' stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    + '<path d="M20.5 14.6A8.5 8.5 0 1 1 9.4 3.5a6.8 6.8 0 0 0 11.1 11.1z"/></svg>';

  document.addEventListener("DOMContentLoaded", function () {
    var btn = document.createElement("button");
    btn.className = "theme-toggle";
    btn.type = "button";
    var sync = function () {
      var isLight = document.documentElement.dataset.theme === "light";
      // Label the destination, not the current state.
      btn.innerHTML = (isLight ? MOON : SUN) + "<span>" + (isLight ? "다크" : "라이트") + "</span>";
      btn.setAttribute("aria-label", isLight ? "다크 테마로 전환" : "라이트 테마로 전환");
      btn.setAttribute("aria-pressed", String(isLight));
    };
    btn.addEventListener("click", function () {
      var next = document.documentElement.dataset.theme === "light" ? "dark" : "light";
      document.documentElement.dataset.theme = next;
      try { localStorage.setItem(KEY, next); } catch (e) {}
      sync();
    });
    sync();
    document.body.appendChild(btn);
  });
})();
