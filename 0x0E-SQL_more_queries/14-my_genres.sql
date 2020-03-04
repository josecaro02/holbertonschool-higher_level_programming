-- Uses hbtn_0d_tvshows to lists all genres of the show Dexter
-- Display tv_genres.name
-- ASC order by genre name
SELECT tv_genres.name
FROM tv_shows INNER JOIN
(
tv_genres INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
)
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
