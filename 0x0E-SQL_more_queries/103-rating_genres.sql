-- Lists all genres in database by rating
-- Display tv_genres.name - rating sum
-- DESC by rating
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_show_ratings INNER JOIN
(tv_shows INNER JOIN
(tv_genres INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id)
ON tv_shows.id = tv_show_genres.show_id)
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC, tv_genres.name ASC;
