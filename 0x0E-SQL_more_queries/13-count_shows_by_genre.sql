-- List all genres from hbtn_0d_tv_shows
-- First column genre
-- Second column number_of_shows
-- Don't show no linked shows
-- Sort DESC bt number of shows
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres INNER JOIN  tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
