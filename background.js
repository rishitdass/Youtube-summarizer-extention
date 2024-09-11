chrome.action.onClicked.addListener((tab) => {
    chrome.tabs.query({ active: true, lastFocusedWindow: true }, (tabs) => {
      let currentUrl = tabs[0].url;
      console.log("Current URL:", currentUrl);
    });
  });
  