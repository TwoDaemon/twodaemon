/*
* Disqus
* To enable on a page, add this JS and a div with id 'disqus_thread' where you want
* the comments thread to appear.
*/

/* Disqus Global Configuration */
var disqus_shortname = 'twodaemon'; // required: replace example with your forum shortname

/* Disqus Function */
(function() {
    var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
    dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
})();
