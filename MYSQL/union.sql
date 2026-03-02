select  first_name,last_name, 'OLD' as Label from parks_and_recreation.employee_demographics
where age>60
union all
select first_name,last_name,'Highly Paid Employee' as Label from 
parks_and_recreation.employee_salary 
where salary>70000;