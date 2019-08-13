/**
 * Created by heyu on 2019/8/13.
 */
chrome.extension.sendMessage({hello: "Cissy"}, function(response) {
    console.log(response.farewell);
});

chrome.tabs.sendMessage(tab.id, {hello: "Cissy"}, function(response) {
    console.log(response.farewell);
});

var bg = chrome.extension.getBackgroundPage();//获取background页面
console.log(bg.a);//调用background的变量或方法。

var pop = chrome.extension.getViews({type:'popup'});//获取popup页面
console.log(pop[0].b);//调用第一个popup的变量或方法。



var bac = chrome.extension.connect({name: "ConToBg"});//建立通道，并给通道命名
bac.postMessage({hello: "Cissy"});var bac = chrome.extension.connect({name: "ConToBg"});//建立通道，并给通道命名
bac.postMessage({hello: "Cissy"});

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {//获取当前Tab
    var cab = chrome.tabs.connect(tabId, {name: "BgToCon"});//建立通道，指定tabId，并命名
    cab.postMessage({ hello: "Cissy"});//利用通道发送一条消息。
};

chrome.extension.onConnect.addListener(function(bac) {//监听是否连接，bac为Port对象
    bac.onMessage.addListener(function(msg) {//监听是否收到消息，msg为消息对象
        console.log(msg.hello);
    })
});