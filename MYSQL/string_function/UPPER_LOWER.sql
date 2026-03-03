select upper("mysql database") ;
select lower("MYSQL");

SELECT d.first_name, UPPER(d.first_name) 
FROM employee_management.demographics ;

SELECT d.first_name, LOWER(d.first_name) 
FROM employee_management.demographics ;