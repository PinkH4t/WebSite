/**** Set Time ***************************************************************/

function time() {
    var date = moment().format('DD-MM-YYYY | h:mm a'); // actual datetime
    var display_date = document.getElementById('date');
    display_date.innerHTML = date;

}
