
var facebook = document.getElementById("facebook-share");
var twitter = document.getElementById("twitter-share");
var pinterest = document.getElementById("pinterest-share");
var linkedin = document.getElementById("linkedin-share");
var tumblr = document.getElementById("tumblr-share");
var reddit = document.getElementById("reddit-share");
var mail = document.getElementById("mail-share");

var title = document.getElementById("header-text").innerText;
var url = document.location.href;
var description = document.querySelector("meta[name~=description][content]").content;

facebook.onclick = function() {
    var fb = window.open("https://www.facebook.com/sharer.php?u=" + url + "&t=" + title);
};

twitter.onclick = function() {
    var tw = window.open("https://twitter.com/share?text=" + title + "&url=" + url);
};

pinterest.onclick = function() {
    var pin = window.open("https://pinterest.com/pin/create/button/?url=" + url + "&description=" + title);
};

linkedin.onclick = function() {
    var ln = window.open("https://linkedin.com/shareArticle?mini=true&title=" + title + "&url=" + url);
};

tumblr.onclick = function() {
    var tum = window.open("https://www.tumblr.com/share/link?url=" + url + "&name=" + title + "&description=" + description);
};

mail.onclick = function() {
    var msg = window.open("mailto:?subject=" + title + "&body=" + url);
};
