parcelRequire=function(e,r,t,n){var i,o="function"==typeof parcelRequire&&parcelRequire,u="function"==typeof require&&require;function f(t,n){if(!r[t]){if(!e[t]){var i="function"==typeof parcelRequire&&parcelRequire;if(!n&&i)return i(t,!0);if(o)return o(t,!0);if(u&&"string"==typeof t)return u(t);var c=new Error("Cannot find module '"+t+"'");throw c.code="MODULE_NOT_FOUND",c}p.resolve=function(r){return e[t][1][r]||r},p.cache={};var l=r[t]=new f.Module(t);e[t][0].call(l.exports,p,l,l.exports,this)}return r[t].exports;function p(e){return f(p.resolve(e))}}f.isParcelRequire=!0,f.Module=function(e){this.id=e,this.bundle=f,this.exports={}},f.modules=e,f.cache=r,f.parent=o,f.register=function(r,t){e[r]=[function(e,r){r.exports=t},{}]};for(var c=0;c<t.length;c++)try{f(t[c])}catch(e){i||(i=e)}if(t.length){var l=f(t[t.length-1]);"object"==typeof exports&&"undefined"!=typeof module?module.exports=l:"function"==typeof define&&define.amd?define(function(){return l}):n&&(this[n]=l)}if(parcelRequire=f,i)throw i;return f}({"Focm":[function(require,module,exports) {
function e(e,t,n){var o=new XMLHttpRequest,r="";for(var i in t)r+=i+"="+t[i]+"&";o.open("GET","/api/"+e.replace("/","")+"?"+r,!0),o.send(),o.onreadystatechange=function(){if(4===o.readyState)return n(o)}}function t(t){e("get_page",{page_name:t},function(e){document.getElementById("content").innerHTML=e.responseText})}function n(){console.log("Started fix...");var e=document.querySelectorAll("a");console.log(e),e.forEach(function(e){e.setAttribute("tab_link",e.getAttribute("href")),e.removeAttribute("href"),e.onclick=function(n){return n.preventDefault(),console.log("Link to",e.getAttribute("tab_link")),t(e.getAttribute("tab_link").replace(".html","")),!1}})}n();
},{}]},{},["Focm"], null)
//# sourceMappingURL=/src.281937c5.js.map