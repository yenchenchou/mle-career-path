# Questions and Answers

## Learning Resources

- [The Ultimate Guide to SQL Interview Questions](https://www.interviewquery.com/blog-sql-interview-questions/)
- [The Facebook Data Engineer Interview](https://towardsdatascience.com/the-facebook-data-engineer-interview-345235afaac0)
- [Ace your data science interview](https://www.interviewquery.com/)
- [Customized for your next interview](https://www.interviewquery.com/pricing)

## Tips Summary from Above

1. Strategies for the live SQL interview
    - Repeat the problem statement
    - Understand the edge cases (Do duplicate events matter? Are we looking at distinct users?)
    - Try working backwards if the problem is tricky
    - Pattern match to different functions
    - Practice
2. The 7 different SQL interview questions
    - Definition based SQL questions
    - Basic SQL questions
        - What's the difference between a LEFT JOIN and an INNER JOIN?
        - When would you use UNION vs UNION ALL? What if there were no duplicates?
        - What's the difference between COUNT and COUNT DISTINCT?
        - When would you use a HAVING clause versus a WHERE clause?
    - Reporting and metrics SQL questions
    - Analytics SQL questions
    - ETL SQL questions
    - Database design questions
    - Logic based SQL questions

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
