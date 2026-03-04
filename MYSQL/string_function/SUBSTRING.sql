#In SQL, the SUBSTRING() function is used to extract part of a string starting from a given position for a specified length
# Syntax - SUBSTRING(expression, start, length)
SELECT first_name as Name,substring(birth_date,6,2) as Birth_Month
FROM demographics;
