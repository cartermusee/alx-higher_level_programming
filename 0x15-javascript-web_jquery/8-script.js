$(function(){
    var $movie = $("UL#list_movies")

   $.ajax({
    type: "GET",
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    success: function (data) {
        $.each(data.results, function (i, item) { 
            $movie.append('<li>'+ item.title + '</li>');
        });
    }
   });
});
