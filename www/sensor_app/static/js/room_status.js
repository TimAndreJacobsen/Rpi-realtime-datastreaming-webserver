const radios = document.forms["range_select"].elements["range_h"];
const range_select_form = document.forms["range_select"];
for(radio in radios) {
    radios[radio].onclick = function(e) {
        range_select_form.submit();
    }
}
// TODO make radio button appear clicked after reload, to indicate to user what data range is being display