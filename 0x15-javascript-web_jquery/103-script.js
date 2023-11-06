$(document).ready(function() { 
    $("INPUT#language_code").keypress(function (e) { 
        if (e.which == 13){
            fetchtranslation();
        }
    });
    $("INPUT#btn_translate").click(function () { 
        fetchtranslation();
    });

    function fetchtranslation(){
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
    }

});
