SELECT first_name, last_name, 'Senior Employee' AS Label
FROM employee_management.demographics
WHERE age > 35

UNION ALL

SELECT d.first_name, d.last_name, 'Highly Paid Employee' AS Label
FROM employee_management.salary s
JOIN employee_management.demographics d
ON s.employee_id = d.employee_id
WHERE s.salary > 80000;