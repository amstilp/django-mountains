var main = function(){

    $('#btn-marmot').click(function() {
        $(this).prop('disabled', true);
        console.log("button pressed");
        var pk;
        console.log("declared variable");
       pk = $(this).attr("data-pk");
       console.log("grabbed variable " + pk);
       $.get('/mountain/see_marmot/', {pk: pk}, function(data){
            console.log(" in $.get");
            $("#n-marmots").text(data);
        });
       $(this).prop('disabled', false);
    });

    $('form').submit(function() {
        $(this).find("#submit-id-submit").prop('disabled',true);
    });
 }

$(document).ready(main);
