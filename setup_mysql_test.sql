-- Create hbnh_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create user 'hbnb_test' w/ pass 'hbnb_test_pwd' for localhost
CREATE USER IF NOT EXISTS 'hbnb_test' @'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges on 'hbnb_test_db' to user 'hbnb_test' at localhost
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test' @'localhost';
-- Grant SELECT prvlg on 'performance_schema' db to 'hbnb_test' usr @ localhost
GRANT SELECT ON performance_schema.* TO 'hbnb_test' @'localhost';
