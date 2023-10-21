-- Script that creates the database hbtn_0d_usa and the table cities
-- cities description: id INT unique, auto generated, NOT NULL and primary key
-- state_id INT not NULL and FOREIGN KEY from state and name VARCHAR(256) cant be NULL
-- If the database or the table already exist the code shouldnt fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (id),
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL);
