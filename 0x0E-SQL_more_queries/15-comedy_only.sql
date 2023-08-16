-- my genres
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres
ON tv_show.id = tv_show_genres.show_id
JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name LIKE '%Comedy%'
ORDER BY tv_show.title ASC
~                            
