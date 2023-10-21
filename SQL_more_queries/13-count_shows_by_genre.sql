-- Script that lists all contained in the database hbtn_0d_tvshows
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre and Second column must be called number_of_shows
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement

SELECT tv_genres.name AS genre, 
       COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
