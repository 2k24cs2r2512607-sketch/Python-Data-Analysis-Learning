#The TRIM() function in SQL removes leading and trailing spaces from a string.
# By default, it behaves like LTRIM(RTRIM(string))
select trim("           sql     ");
select ltrim("             DBMS     ");
select rtrim("           DATA               ");

#Removing specific characters You can pass a set of characters to remove instead of just spaces:
select trim('$$' FROM '    $Database$      ') AS TrimmedString;
