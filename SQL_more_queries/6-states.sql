-- Script that creates the database hbtn_0d_usa and the table states
-- states description: id INT unique, auto generated, NOT NULL and primary key
-- and name VARCHAR(256) cant be NULL
-- If the database or the table already exist the code shouldnt fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (id),
	name VARCHAR(256) NOT NULL);
