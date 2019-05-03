const radios = document.forms["range_select"].elements["range_h"];
const range_select_form = document.forms["range_select"];
for(radio in radios) {
    radios[radio].onclick = function(e) {
        range_select_form.submit();
    }
}