$(document).ready(function() { 
    $("DIV#add_item").on('click', function () {
        $("UL.my_list").append('<li>Item</li>');
    });
    $('DIV#remove_item').click(function () { 
        $("UL.my_list li").remove(':last');
        
    });
    $('DIV#clear_list').click(function () { 
        $("UL.my_list li").remove();
        
    });


});
