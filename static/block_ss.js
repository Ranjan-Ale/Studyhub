/*

document.addEventListener("DOMContentLoaded", function () {
  const userIdentifier = window.userIdentifier || "Guest";

  // --- Watermark setup ---
  const wm = document.createElement("div");
  wm.className = "watermark";
  wm.textContent = userIdentifier + " • " + new Date().toLocaleString();
  document.body.appendChild(wm);

  // --- Styles ---
  const style = document.createElement("style");
  style.textContent = `
    .watermark {
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) rotate(-25deg);
      font-size: 5rem;
      color: rgba(0,0,0,0.07);
      pointer-events: none;
      z-index: 9999;
      white-space: nowrap;
      user-select: none;
    }
    .blur-overlay {
      position: fixed;
      inset: 0;
      backdrop-filter: blur(8px);
      background: rgba(255,255,255,0.3);
      z-index: 9998;
      display: none;
      pointer-events: none;
    }
  `;
  document.head.appendChild(style);

  // --- Blur overlay ---
  const blur = document.createElement("div");
  blur.className = "blur-overlay";
  document.body.appendChild(blur);

  // --- Disable right-click ---
  document.addEventListener("contextmenu", (e) => e.preventDefault());

  // --- Try to block PrintScreen (not reliable) ---
  window.addEventListener("keydown", (e) => {
    if (e.key === "PrintScreen") {
      e.preventDefault();
      try {
        navigator.clipboard.writeText("");
      } catch {}
      alert("Screenshots are discouraged on this page.");
    }
  });

  // --- Blur when page not active ---
  document.addEventListener("visibilitychange", () => {
    blur.style.display = document.hidden ? "block" : "none";
  });
  window.addEventListener("blur", () => (blur.style.display = "block"));
  window.addEventListener("focus", () => (blur.style.display = "none"));
});


*/