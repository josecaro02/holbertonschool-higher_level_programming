-- List all Comedy shows in database hbtn_0d_tvshows
-- Display tv_shows.title
-- Results ASC order
SELECT tv_shows.title
FROM tv_genres INNER JOIN
(tv_shows INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id)
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
