-- my genres
SELECT name
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_show.id = tv_show_genres.genre_id
WHERE tv_shows.title LIKE '%Dexter%'
ORDER BY tv_genres.name ASC
