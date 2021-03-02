-- lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each
SELECT a.name AS genre, count(b.genre_id) AS number_of_shows
FROM tv_genres a
LEFT JOIN tv_show_genres b ON a.id = b.genre_id
GROUP BY a.name
HAVING number_of_shows > 0
ORDER by number_of_shows DESC;
