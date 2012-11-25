function DayConv(_D) {
	var D = (_D <= 9 && _D >= 0) ? ("0" + _D) : _D;
	return D;
};


function dispDateTime() {
	// image tick
    var MonthArr = new Array("Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık")
    var WeekDayArr = new Array("Pazar","Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi")
    var BandDate = new Date();
    var StrWeekDay = BandDate.getDay();
    var StrDay = BandDate.getDate();
    var StrMonth = BandDate.getMonth();
    var StrYear = BandDate.getFullYear();
    var StrHour = BandDate.getHours();
    var StrMinute = BandDate.getMinutes();
  
    $("#main-datetime").html(DayConv(StrDay)+" "+MonthArr[StrMonth]+" "+StrYear+  ', '+ StrHour+":"+DayConv(StrMinute));
};

$(document).ready(function(){
    dispDateTime();
});
