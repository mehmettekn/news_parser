$(document).ready(function () {
    var datasets = {};    
	
    // Caching some of the selectors for better performance
	var periodDropDown = $('#periodDropDown'),
		dropDownUL = $('ul',periodDropDown),
		currentPeriod = $('.currentPeriod',periodDropDown),
		performancePlot = $('#placeholder'),
		cache = {};    

    // Listening for clicks on the dropdown:
	periodDropDown.find('li').click(function(){
		var li = $(this);
		currentPeriod.text(li.text());
		loadPeriod(li.data('action'));
	});
	
	// Disabling the dropdown when an AJAX request is active:
	periodDropDown.ajaxStart(function(){
		periodDropDown.addClass('inactive');
	}).ajaxComplete(function(){
		periodDropDown.removeClass('inactive');
	});

   // Loading the data for the lasthour on page load:
	loadPeriod('lasthour');

	var currentData,
        choiceFlag = false;
	    	
    // This function fetches and caches AJAX data.
	function loadPeriod(period){

		// If the period exists in cache, return it.
		if(cache[period]){
			render(cache[period]);
		}
		else{
			
			// Otherwise initiate an AJAX request:
			$.get('/stats/'+period+'/',function(r){
				cache[period] = r;
				render(r);
			},'json');		
		}

        function render(obj){
            $.each(obj, function(key, value){
                datasets[key] = {};
                datasets[key]['label'] = value.label;
                datasets[key]['data'] = value.data;
                });
    
            console.log(datasets)
            // hard-code color indices to prevent them from shifting as
            // countries are turned on/off
            var i = 0;
            $.each(datasets, function(key, val) {
                val.color = i;
                ++i;
                });
        
            // insert checkboxes 
            var choiceContainer = $("#choices");
            if (choiceFlag == false){            
                $.each(datasets, function(key, val) {
                choiceContainer.append('<br/><input type="checkbox" name="' + key +
                                       '" checked="checked" id="id' + key + '">' +
                                       '<label for="id' + key + '">'
                                       + val.label + '</label>');
                choiceFlag = true
                });
            };
    
            choiceContainer.find("input").click(plotAccordingToChoices);
           
            function plotAccordingToChoices() {
                var data = [];

                choiceContainer.find("input:checked").each(function () {
                    var key = $(this).attr("name");
                    if (key && datasets[key])
                        data.push(datasets[key]);
                });

                if (data.length > 0)
                    $.plot(performancePlot, data,  
                        {
                            xaxis:{ mode:"time"}                            
                        }                       
                    );
            }

            plotAccordingToChoices();
        };           		         
    };
    
});
    
