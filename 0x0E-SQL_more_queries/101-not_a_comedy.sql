-- List all shows without genre Comedy
-- Display tv_shows.title
-- Result ASC
SELECT tv_shows.title
FROM tv_shows LEFT JOIN
(SELECT tv_shows.title AS title
FROM tv_shows INNER JOIN
(tv_show_genres INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id)
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = 'Comedy') AS comedy_titles
ON tv_shows.title = comedy_titles.title
WHERE comedy_titles.title IS NULL
ORDER BY tv_shows.title ASC;
