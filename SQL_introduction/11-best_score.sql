-- List all records with a score >= 10 in second_table, showing score and name, ordered by score descending
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
