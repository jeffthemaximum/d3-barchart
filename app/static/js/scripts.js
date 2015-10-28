$(document).ready(function(){
    $('#form').submit(function (evt) {
        evt.preventDefault();
        
        var search = $("input[name=name]").val();
        $.get("/github/" + search, function(data){
            var ret = $.parseJSON(data);
            console.log(ret);
            $( "#bar-chart" ).append( "<p>Here's the output when you search for <b>" + search + "</b>:</p>" );
            $( "#bar-chart" ).append( "<p>" + JSON.stringify(ret, null, 4) + "</p>" );
        });

    });
});
