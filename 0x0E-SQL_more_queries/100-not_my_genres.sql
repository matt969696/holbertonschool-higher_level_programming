-- uses the hbtn_0d_tvshows database
-- to list all genres not linked to the show Dexter
SELECT d.name
FROM tv_genres d
WHERE d.name NOT IN (SELECT a.name
FROM tv_genres a
LEFT JOIN tv_show_genres b ON a.id = b.genre_id
LEFT JOIN tv_shows c ON b.show_id = c.id
WHERE c.title = 'Dexter')
ORDER BY name;
