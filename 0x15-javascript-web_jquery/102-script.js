$(document).ready(function() { 
    $("INPUT#btn_translate").click(function () { 
        var languagecode = $("INPUT#language_code").val()

        $.ajax({
            type: "GET",
            url: "https://www.fourtonfish.com/hellosalut/hello/",
            data: {lang:languagecode},
            success: function (response) {
                $("DIV#hello").text(response.hello);
            },
            error: function(xhr,status, error){
                $('div#hello').text("Error fetching translation"  + error); 
            }
        });
        
    });

});
