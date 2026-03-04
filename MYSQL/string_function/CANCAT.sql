# CONCAT() is a function used to join (concatenate) two or more strings into one.
# Syntax - CONCAT(string1, string2, ..., stringN)
select first_name,last_name,CONCAT(first_name," ",last_name) as Full_Name
from demographics;