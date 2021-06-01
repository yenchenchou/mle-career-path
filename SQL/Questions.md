# Questions and Answers

1. self join:
    - when idetify columns where you need to compare some columns that need to be compare, for example identify companies that received an investment from Great Britain following an investment from Japan.
2. n th highest/lowest value:

    ```SQL
    # Write your MySQL query statement below
    SELECT
        (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
    ;
    # Better solution
    select max(salary) as SecondHighestSalary
    from Employee
    where salary < (select max(salary) from Employee)
    ```
