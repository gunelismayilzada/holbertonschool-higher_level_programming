-- List all records of second_table where name is not NULL, showing score and name, ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
