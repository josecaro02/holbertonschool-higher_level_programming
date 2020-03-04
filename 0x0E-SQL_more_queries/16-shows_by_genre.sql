-- List all show and all genres linked to that show
-- NULL if show dont have a genre
-- Display tv_shows.title - tv_genres.name
-- Results ASC by show_title and genre_name
SELECT tv_shows.title, tv_genres.name
FROM tv_shows LEFT JOIN
(tv_genres INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id)
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
