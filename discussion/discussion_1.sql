SELECT department_name AS department_name,
AVG(people.popularity) AS average_popularity,
COUNT(people_id) AS total_people
FROM department
JOIN people
ON department.department_id = people.department_id
GROUP BY department.department_id, department_name
HAVING COUNT(people_id) < 50
ORDER BY average_popularity DESC;
