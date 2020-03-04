-- List all genres not linked to show Dexter
-- Each record should display tv_genres.name
-- Result ASC order
SELECT tv_genres.name
FROM tv_genres LEFT JOIN
(SELECT tv_genres.name, tv_genres.id AS id_genre
FROM tv_shows INNER JOIN
(tv_show_genres INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id)
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter') AS dexter_genres
ON tv_genres.id = dexter_genres.id_genre
WHERE dexter_genres.id_genre IS NULL
ORDER BY tv_genres.name ASC;
