SELECT name, popularity, department_id
FROM people
WHERE department_id = 1
ORDER BY popularity DESC
LIMIT 10;
