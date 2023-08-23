-- Script that import database from a table dump

SELECT temperatures.city, 
AVG(temperatures.value) AS average
FROM temperatures
GROUP BY temperatures.city
ORDER BY average DESC;
