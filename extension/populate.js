function appendSelection(text) {
    console.log("this works");
    
    var selectedTextList = document.getElementById('user-selections');
    var listItem = document.createElement('div');
    listItem.classList.add('list-item');
    var listP = document.createElement('p');
    var listText = document.createTextNode(text);
    listP.appendChild(listText);
    listItem.appendChild(listP);
    selectedTextList.appendChild(listItem);
}

chrome.storage.sync.get('selectedText', function(data) {
    console.log("getting data: " + data);
});