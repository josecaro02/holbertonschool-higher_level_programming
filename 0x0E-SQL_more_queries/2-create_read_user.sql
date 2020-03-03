-- Creates a databes hbtn_0d_2 and the user user_0d_2
-- Only SELECT privileges for user in the database
-- not fail if dabase of user exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

USE hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
