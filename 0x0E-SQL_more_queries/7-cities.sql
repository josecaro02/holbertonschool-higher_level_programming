-- Creates the database hbtn_0d_usa and table cities
-- cities id INT AUTO INCREMENT NOT NULL AND PRIMARY KEY
-- state_id NOT NULL, FOREIGN KEY references  id of states
-- name VARCHAR(256) NOT NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities
       (id INT NOT NULL UNIQUE AUTO_INCREMENT,
       state_id INT NOT NULL,
       name VARCHAR(256),
       PRIMARY KEY(id),
       FOREIGN KEY (state_id) REFERENCES states(id));
