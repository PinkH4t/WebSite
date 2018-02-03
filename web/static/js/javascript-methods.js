/**** Set Time ***************************************************************/

function time() {
    moment.locale('fr');
    var date = moment().format('lll'); // actual datetime
    var display_date = document.getElementById('date');
    display_date.innerHTML = date;

}
