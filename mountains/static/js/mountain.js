var main = function(){

    $('#btn-marmot').click(function() {
        console.log("button pressed");
        var pk;
        console.log("declared variable");
       pk = $(this).attr("data-pk");
       console.log("grabbed variable " + pk);
       $.get('/mountain/see_marmot/', {pk: pk}, function(data){
            console.log(" in $.get");
            $("#n-marmots").text(data);
        });
    });
};

$(document).ready(main);