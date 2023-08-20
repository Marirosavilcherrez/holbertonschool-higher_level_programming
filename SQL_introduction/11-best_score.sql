-- Script that list all records of with score >=10
-- from the table second table in the database hbtn_0c_0

SELECT score, name FROM second_table WHERE score >=10 ORDER BY score DESC;

