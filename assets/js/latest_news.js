var latestNews = {};
var latestNewsString = '\
                    <li>Son Dakika Haberler &nbsp;&nbsp;&nbsp;&nbsp;</li>\
                        ';
var preloader1 = $('#latest-preloader');

function render1(obj){
    $.each(obj["POSTS"], function(key, value){
        latestNewsString += '\
            <li>\
    <span class="news-src">' + value.SRC + '</span><span class="news-pubdate">' + value.PUBDATE + '</span><span class="news-title"><a href="' + value.LINK + '" target="_blank">' + value.TITLE + '</a></span>\
            </li>'
    });
    $('#latest-ticker').html(latestNewsString);
    initTicker1();
}

function initTicker1(){
    $(function(){
        $('#latest-ticker').liScroll();
        console.log("latest news ticker initiated");
        preloader1.removeClass('preloader');
    });
}

function loadJSON1(){
    $.getJSON('/json/latest_news', function(data){
        console.log("latest news json loaded")        
        render1(data);
    }).error(function(){
        console.log("latest news json loading error");
    }).complete(function(){
        setTimeout(loadJSON1, 3000000)
    });
};

loadJSON1();

