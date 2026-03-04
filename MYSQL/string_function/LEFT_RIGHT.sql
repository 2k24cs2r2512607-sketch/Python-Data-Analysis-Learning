#The LEFT() and RIGHT() functions in SQL are used to extract a specific number of characters from a string — 
#either starting from the left or from the right side.
SELECT  first_name,LEFT(first_name,3),RIGHT(first_name,3)
FROM demographics;

 
 