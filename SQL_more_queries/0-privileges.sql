-- 0-privileges.sql
-- List all privileges of user_0d_1 and user_0d_2 on localhost

-- Make sure the users exist (you can skip this if already created)
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Optionally, grant some privileges for testing
-- GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';

-- Show privileges for both users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
