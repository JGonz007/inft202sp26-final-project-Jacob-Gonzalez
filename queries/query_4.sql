SELECT department_id, AVG(popularity), COUNT (*)
FROM people
GROUP BY department_id
HAVING AVG(popularity) > 2
AND COUNT (*) >= 10
ORDER BY AVG(popularity) DESC;
