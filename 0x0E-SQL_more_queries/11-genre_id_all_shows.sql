-- Lists all shows by tv_shows.title and tv_show_genres.genre_id
-- Results sorted ASC by tv_shows.title and tv_show_genres.genre_id
-- NULL if show doesn't have a genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
