SELECT department_id, AVG(popularity)
FROM people
GROUP BY department_id
ORDER BY AVG(popularity) DESC;
