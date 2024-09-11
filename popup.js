
import { getSummary } from './post_for_summary.js';

document.addEventListener("DOMContentLoaded", () => {
  chrome.tabs.query({ active: true, lastFocusedWindow: true }, (tabs) => {
    let currentUrl = tabs[0].url;
    getSummary("http://127.0.0.1:5000/summarize", currentUrl);
  });
  
});
