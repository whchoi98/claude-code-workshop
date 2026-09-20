/* Adapter for the existing HTML lessons and the shared My Workshop reader. */
(() => {
  "use strict";
  const outline = document.querySelector("[data-page-toc]");
  const compact = window.matchMedia("(max-width: 1250px)");
  // A desktop outline must remain visible after resizing a collapsed mobile view.
  compact.addEventListener("change", () => {
    if (outline) outline.open = !compact.matches;
  });
})();
