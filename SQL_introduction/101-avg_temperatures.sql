-- Script that import database from a table dump

SELECT temperatures.city, 
AVG(temperatures.value) AS avg_temp
FROM temperatures
GROUP BY temperatures.city
ORDER BY avg_temp DESC;
