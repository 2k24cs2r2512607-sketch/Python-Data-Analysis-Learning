# Increase Salary
-- < 50000 = 5%
-- > 50000 = 7%
-- Finance = 10%
select d.first_name,dept.department_name,s.salary,
case when s.salary<50000 then s.salary+s.salary*(0.05)
when s.salary>50000 then s.salary+s.salary*(0.07)
when dept.department_name="Finance" then s.salary+s.salary*(0.1) 
end as New_Salary from demographics d join salary s 
on d.employee_id=s.employee_id
join departments dept on s.dept_id=dept.department_id; 