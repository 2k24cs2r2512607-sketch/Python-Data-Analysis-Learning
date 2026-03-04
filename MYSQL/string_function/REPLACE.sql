#The REPLACE function in SQL is used to substitute all occurrences of a specified substring within a string with another substring. 
# Syntax - REPLACE(string_expression, search_string, replacement_string)
SELECT REPLACE("I am learning SQL","I am","We are") as Message;
SELECT first_name,REPLACE(first_name,"a","A") as Replace_a_with_A from demographics;
