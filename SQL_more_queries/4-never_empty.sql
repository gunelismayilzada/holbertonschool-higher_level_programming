-- 4-never_empty.sql
-- Create table id_not_null with id (default 1, not null) and name columns
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
