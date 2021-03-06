var imkb = {},
    imkbString = '',
    cache = {};

var downSymbol = "▼",
    upSymbol = "▲",
    symbol = "";

var preloader = $('#imkb-preloader');

function render(obj){
    console.log('render in process');
    $.each(obj['ENDEKS'], function(key, value){
        if (value.CLASS == "DOWN"){
            symbol = downSymbol;
        }else{
            symbol = upSymbol;
        };
                
        imkbString += '\
            <li>\
                       <span class="imkb-ticker-name">' + value.NAME + '</span><span class="imkb-ticker-value">' + value.ASK + '</span><span class="' + value.CLASS +'">'+ symbol +'&nbsp;&nbsp;&nbsp;&nbsp;</span>\
            </li>';
    });
    $('#imkb-ticker').html(imkbString);   
    initTicker();
}



function initTicker(){   
    $(function(){
        $('#imkb-ticker').liScroll({travelocity: 0.15});
        preloader.removeClass('preloader');
    });
}


function loadJSON(){
        
    if (cache['imkb']){
        console.log('data loaded from cache');        
        data = cache['imkb'];
        render(data);
    }else{
        $.getJSON('/json/imkb_endeks', function(data){
            console.log('JSON loaded');
            preloader.removeClass('preloader');            
            render(data);
        }).error(function(){
            console.log('JSON loading error');
            loadJSON();
        }).complete(function(){
            setTimeout(loadJSON, 3000000)
        });
    };
}   

loadJSON();



