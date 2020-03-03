-- List the number of records with the same score
-- in the table seconde_table
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score HAVING COUNT(*) ORDER BY score DESC;
