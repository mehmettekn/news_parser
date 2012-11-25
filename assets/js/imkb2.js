$(document).ready(function(){
    var preloader = $('#preloader'),
        imkbTicker = $('#imkb-ticker');

    function initTicker(){   
        $(function(){
           imkbTicker.liScroll();
           preloader.removeClass('preloader');
           imkbTicker.removeClass('imkb-ticker');             
        });
    };

    initTicker();
});
