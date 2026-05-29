SELECT department_name AS department_name,
COUNT(people_id) AS high_popularity_count
FROM department
JOIN people
ON department.department_id = people.department_id
WHERE people.popularity > 10
GROUP BY department.department_id, department.department_name
ORDER BY high_popularity_count DESC;
