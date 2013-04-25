/*global $, jQuery, document*/

function check_submit(v) {
    "use strict";
    $('input').removeAttr('checked');
    $('input[value=' + v + ']').prop('checked', true);
    $('#voting_form').submit();
}

$(document).ready(function () {
    "use strict";
    if ($('input[value="-1"]').is(':checked')) {
        $('#button-no').addClass('disabled');
    } else if ($('input[value="1"]').is(':checked')) {
        $('#button-yes').addClass('disabled');
    }

    $('#button-no').click(function () {check_submit("-1"); });
    $('#button-yes').click(function () {check_submit("1"); });
});