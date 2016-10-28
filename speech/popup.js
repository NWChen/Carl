console.log("loaded");

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
	check();
});

chrome.tabs.onCreated.addListener(function(tabId, changeInfo, tab) {         
	check();
});

function check(){	
	chrome.tabs.getAllInWindow(null, function(tabs){
		tabs.forEach(function(tab){
			if(tab.url=="https://www.facebook.com/") {
				console.log("THATSHIT");
				document.getElementById("url").innerHTML=tab.url;
			}
		});
	});
};
