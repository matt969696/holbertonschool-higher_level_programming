-- lists all genres from hbtn_0d_tvshows_rate
-- by their rating
SELECT a.name, sum(c.rate) AS rating
FROM tv_genres a
LEFT JOIN tv_show_genres b ON a.id = b.genre_id
LEFT JOIN tv_show_ratings c ON b.show_id = c.show_id
GROUP BY a.name
ORDER BY rating DESC;
