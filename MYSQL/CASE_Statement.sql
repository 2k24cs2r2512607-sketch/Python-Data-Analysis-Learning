#The CASE statement in SQL lets you apply conditional logic inside queries, similar to an if-then-else structure.
select first_name,age, case 
WHEN age<=30 then "YOUNG ADULTS"
when age BETWEEN 31 AND 39 then "OLD"
else "On Death's Door" end as Label
from demographics;
 