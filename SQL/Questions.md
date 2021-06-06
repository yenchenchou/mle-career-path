# Questions and Answers

1. self join:
    - when idetify columns where you need to compare some columns that need to be compare, for example identify companies that received an investment from Great Britain following an investment from Japan.

    ```SQL
    SELECT DISTINCT japan_investments.company_name,
        japan_investments.company_permalink
    FROM tutorial.crunchbase_investments_part1 japan_investments
    JOIN tutorial.crunchbase_investments_part1 gb_investments
        ON japan_investments.company_name = gb_investments.company_name
    AND gb_investments.investor_country_code = 'GBR'
    AND gb_investments.funded_at > japan_investments.funded_at
    WHERE japan_investments.investor_country_code = 'JPN'
    ORDER BY 1
    ```

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
