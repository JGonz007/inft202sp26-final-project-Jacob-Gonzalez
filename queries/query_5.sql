SELECT people.name, people.popularity, department.department_name
FROM people
JOIN department
ON department.department_id = people.department_id
ORDER BY people.popularity DESC
LIMIT 20;
