-- lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.
SELECT s.title, g.genre_id
FROM tv_shows s
RIGHT JOIN tv_show_genres g on s.id = g.show_id
ORDER BY s.title, g.genre_id;
