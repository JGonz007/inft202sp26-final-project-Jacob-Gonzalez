SELECT department.department_name,
AVG(people.popularity) AS average_popularity,
COUNT(people.people_id) AS total_people
FROM department
JOIN people
ON department.department_id = people.department_id
GROUP BY department.department_name
ORDER BY average_popularity DESC;
