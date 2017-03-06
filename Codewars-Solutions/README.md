# Codewars-Solutions

Website - https://www.codewars.com

My profile - https://www.codewars.com/users/S!D


@Matt c

Description / Question
#Correct the code.

We want to display the Firstname, Lastname and Company of the employees
who are not from India.

**Employee Table Schema**

- eid
- firstname
- lasname
- company
- country

**Select Table Schema**

- fname
- lname
- company


Solution

SELECT firstname AS fname, lastname AS lname, company
FROM employee
WHERE country <> 'India' ;


HELP ME WRITE THE TEST CASES.
Thanks.
