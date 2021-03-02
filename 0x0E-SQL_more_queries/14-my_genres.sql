-- uses the hbtn_0d_tvshows database
-- to lists all genres of the show Dexter
SELECT a.name
FROM tv_genres a
LEFT JOIN tv_show_genres b on a.id = b.genre_id
LEFT JOIN tv_shows c on b.show_id = c.id
WHERE c.title = 'Dexter'
ORDER by name;
