/**** Set Time ***************************************************************/

function addZero(i) {
if (i < 10) { //add zero in front of date number < 10
i = "0" + i;
}
return i;
}

function time() {
    var date = moment().format('MMMM Do YYYY, h:mm:ss a'); // actual datetime
    var display_date = document.getElementById('date');
    display_date.innerHTML = date;
    setTimeout("time()", 3000);
    window.onload=time();

}
