#Return name of countries containing the substring "s" and with population great than “p”

SELECT name FROM table WHERE CONTAINS (column, 's') AND population > p;

#If I had all the names of the columns I would do something like this:
SELECT name 
FROM table 
WHERE (CONTAINS (column1, 's') OR CONTAINS (column2, 's') CONTAINS (column3, 's'))
AND population > p;