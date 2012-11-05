$(document).ready(function(){
	
	// Caching some of the selectors for better performance
	var periodDropDown = $('#periodDropDown'),
		dropDownUL = $('ul',periodDropDown),
		currentPeriod = $('.currentPeriod',periodDropDown),
		performancePlot = $('#plot'),
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
	
	// Binding a custom "render" event to the plot div:
	
	performancePlot.bind('render',function(e,plotData,labels){

		var ticksLength = 7;

		// Using the Flot jQuery plugin to generate
		// the performance graph:
		
		var plot = $.plot(performancePlot,
			[{
				// Passing the datapoints received as a parameter
				// and setting the color and legend label.
				
				data: plotData,
				color:'#86c9ff',
				label: "Response Time"
			}], {
				series: {
					// Setting additional options for the styling.
					lines: {
						show:true,
						fill:true,
						fillColor:'rgba(237,247,255,0.4)',
						lineWidth:1
					},
					shadowSize: 0,
					points: { show: (labels.length == 1) }
				},
				grid: {
					tickColor:'#e0e0e0',
					hoverable: true,
					borderWidth:1,
					borderColor:'#cccccc'
				},
				xaxis:{
					
					// This function is called by the plugin
					// which passes a "range" object. The function
					// must generate an array with the divisions ticks:
					
					ticks:function(range){

						ticksLength = range.max-range.min;
						var dv = 1;
						
						// Trying to find a suitable number of ticks,
						// given the varying number of data points in the
						// graph:
						
						while(ticksLength>12){
							ticksLength = Math.floor(ticksLength/++dv);
							if(dv>30) break;
						}
						
						var ratio = (range.max-range.min)/ticksLength,
							ret = [];
							
						ticksLength++;
						
						for(var i=0;i<ticksLength;i++){
							ret.push(Math.floor(i*ratio));
						}
						
						return ret;
					}
				}
				
		});
		
		// The Flot plugin has some limitations. In the snippet below
		// we are replacing the ticks with proper, more descriptive lables:
		
		var elem = $('div.tickLabel').slice(0,ticksLength).each(function(){
			var l = $(this);
			l.text(labels[parseInt(l.text())]);
		}).last().next().hide();
		
		
		// Displaying a tooltip over the points of the plot:
		
		var prev = null;
		performancePlot.bind("plothover", function (e,pos,item) {

			if (item) {

				if(item.datapoint.toString() == prev){
					return;
				}
				
				prev = item.datapoint.toString();
				
				// Calling the show method of the tooltip object,
				// with X and Y coordinates, and a tooltip text:
				
				tooltip.show(
					item.pageX,
					item.pageY,
					currentData.chart.tooltip.replace('%2',item.datapoint[1])
											 .replace('%1',currentData.chart.data[item.dataIndex].label)
				);
			}
			else {
				tooltip.hide();
				prev = null;
			}

		});
	
	}).bind("mouseleave",function(){
		tooltip.hide();
		prev = null;
	});
	
	// This object provides methods for hiding and showing the tooltip:
	
	var tooltip = {
		show : function(x, y, str) {

			if(!this.tooltipObj){
				this.tooltipObj = $('<div>',{
					id		: 'plotTooltip',
					html	: str,
					css		: {
						opacity	: 0.75
					}
				}).appendTo("body");
			}
			
			this.tooltipObj.hide().html(str);
			var width = this.tooltipObj.outerWidth();
			
			this.tooltipObj.css({left: x-width/2, top: y+15}).fadeIn(200);
		},
		hide : function(){
			$("#plotTooltip").hide();
		}
	}

	// Loading the data for the last 24hours on page load:
	loadPeriod('24hours');


	var currentData;
	
	// This function fetches and caches AJAX data.
	function loadPeriod(period){

		// If the period exists in cache, return it.
		if(cache[period]){
			render(cache[period]);
		}
		else{
			
			// Otherwise initiate an AJAX request:
			$.get('/ajax/'+period+'/',function(r){
				cache[period] = r;
				render(r);
			},'json');		
		}
		
		function render(obj){

			var plotData = [],
				labels = [],
				downtimeData = $('#downtimeData');
			
			// Generating plotData and labels arrays.
			$.each(obj.chart.data,function(i){
				plotData.push([i,this.value]);
				labels.push(this.label);
			});
			
			// They are passed with our custom "render" event to the plot:
			performancePlot.trigger('render',[plotData, labels]);
			
			// Formatting the downtime:
			if(obj.downtime.length){
				
				$('#noDowntime').hide();

				if(!obj.processed){
					// Adding the heading for the downtime list:
					obj.downtime.push({begin: 'FROM',end:'TO',period:'DURATION'});
					obj.downtime = obj.downtime.reverse();
				}
				obj.processed = true;
				
				var tmp = $('<div class="dtContainer">'),
					className = '';
				
				$.each(obj.downtime,function(){
					if(this.end == 'NOW'){
						className = ' ongoing';
					}
					else className = '';
					
					tmp.append(
						'<div class="row'+className+'">'+
							'<span class="from">'+this.begin+'</span>'+
							'<span class="to">'+this.end+'</span>'+
							'<span class="period">'+this.period+'</span>'
						+'</div>'
					);
				});
				
				downtimeData.html(tmp)
			}
			else {
				downtimeData.empty();
				$('#noDowntime').show();
			}
			
			currentData = obj;
		}
	}
});
