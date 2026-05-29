SELECT department_id, COUNT(*)
FROM people
GROUP BY department_id
ORDER BY COUNT(*) DESC;
