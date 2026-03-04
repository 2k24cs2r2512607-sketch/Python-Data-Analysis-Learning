#The MySQL LOCATE() function is used to find the position of the first occurrence of a substring within a string.
# If the substring is not found, it returns 0.
SELECT LOCATE("B","DATABASE");
SELECT first_name,LOCATE("ra",first_name)
from demographics;