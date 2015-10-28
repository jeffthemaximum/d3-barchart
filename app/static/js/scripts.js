$(document).ready(function(){
    $('#form').submit(function (evt) {
        evt.preventDefault();
        
        var search = $("input[name=name]").val();
        $.get("/github/" + search, function(data){
            debugger;
            var ret = $.parseJSON(data);
            console.log(ret)
        });

    });
});
