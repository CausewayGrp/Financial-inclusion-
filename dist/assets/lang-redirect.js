// Root entry route (the hreflang x-default): open the edition the reader chose before, otherwise Arabic.
// A separate file, not an inline script, so a strict Content-Security-Policy (script-src 'self') can apply everywhere.
(function(){var l="ar";try{var s=localStorage.getItem("yfie-lang");if(s==="en"||s==="ar")l=s;}catch(e){}location.replace("/"+l+"/");})();
