-- Script that import database from a table dump

SELECT city, AVG((temperature * 9/5) + 32) AS avg_temperature_fahrenheit
FROM temperatures
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC;

