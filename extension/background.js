chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.sync.set({color: '##cc6bef'}, function() {
      console.log("The highlighter color is light purple.");
    });

    chrome.storage.sync.set({selectedText: []}, function() {
      console.log("Selected text init");
    });
    chrome.storage.sync.set({recording: false}, function() {
      console.log("not recording");
    });
    
/*
    chrome.browserAction.onClicked.addEventListener('click', function(tab) {
      chrome.tabs.query({active: true, lastFocusedWindow: true}, function (tabs) {
          var url = tabs[0].url;
          alert(url);
      
          var http = new XMLHttpRequest();
          var server = 'http://localhost:8000/intellihistory/keywords';
          var data = new FormData();
          data.append('url', url);
          http.open('POST', server, true);
          //http.setRequestHeader('Content-type', 'multipart/form-data');
          http.onreadystatechange = function() {//Call a function when the state changes.
              if(http.readyState == 4 && http.status == 200) {
                  console.log('ready state change');
              }
          };
      
          http.onload = function () {
            // do something to response
            alert(this.responseText);
          };
      
          http.send(data);
          
      
      });
  });
  */

  });

  
  