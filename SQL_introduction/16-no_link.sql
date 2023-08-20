-- Script that lists all records of table second_table

DELETE FROM second_table WHERE name = "George";
INSERT INTO second_table (score, name) VALUES(18, "Aria");
INSERT INTO second_table (score, name) VALUES(12, "Aria");
SELECT score, name FROM second_table ORDER BY score DESC;


