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

3. n th highest/lowest value:

    ```SQL
    -- Write your MySQL query statement below
    SELECT
        (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
    ;
    -- Better solution
    select max(salary) as SecondHighestSalary
    from Employee
    where salary < (select max(salary) from Employee)
    ```

## SQL clause use case scenario and tips

### When to use JOIN

1. self join: table references data in itself.

    - An `Employee` table that have `SupervisorID` column that points to the employee that is the boss of the current employee.
    - identify companies that received an investment from Great Britain following an investment from Japan.

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

    -
2. Inner join
    - count unique users for product view

        ```SQL
        -- t_pages: page_id, product_id
        -- t_users: user_id, page_id, timestamp
        select 
            a.product_id,
            count(distinct b.user_id) as user_view
        from t_pages a
        join t_users b on a.page_id = b.page_id
        group by 1
        order by 2     
        ```

### When to use aggregation

1. Without `group by`:
    - get the max salary at 2020:

        ```SQL
        select max(salary) as salary 
        from employee_table 
        where year = 2020;
        ```

    - What if you want the employee name with max salary at 2020: use subquery

        ```SQL
        select name, salary 
        from employee_table
        where salary = (
            select max(salary) as salary from employee_table where year = 2020
            )
        ```

    - Get min, max, mean score

        ```SQL
        select min(score), max(score), avg(score)
        from data
        ```

### When to use EXIST/IN/JOIN

1. EXIST: When you just want the columns from one table but need filters/conditions from other tables. You can still use join but not efficient
    - Find customers who have at least one payment whose amount is greater than 11 [see details](https://www.postgresqltutorial.com/postgresql-exists/)

        ```SQL
        -- use exists
        select name
        from customer c
        where exists (
            select 1
            from payment p
            where p.customer_id = c.customer_id and amount > 11
        )
        order by 1

        -- use join
        with tmp as (
            select distinct customer_id
            from payment
            where amount > 11
        )
        select c.name as name
        from customer c
        inner join tmp p
            on c.customer_id = p.customer_id
        order by 1
        ```

### When to use CTE (with)

1. query too complex
    - Product view distribution of each product: product_view, # of users

        ```SQL
        -- t_pages: page_id, product_id
        -- t_users: user_id, page_id, timestamp

        -- get the views of each user + product
        -- get product view for each diistinct user
        with user_views as (
            select a.product_id, b.user_id, count(a.page_id) as views
            from t_pages a
            join t_users b on a.page_id = b.page_id
            group by 1, 2
        )
        select product_id, views, count(distinct user_id) as users
        from user_views
        group by 1, 2
        ```

## Qestions by scenario

### Social Network

```SQL
highschooler ('id', 'name', 'grade')
friend ('id1', 'id2')
likes ('id1', 'id2')
```

1. Find the names of all students who are friends with someone names Gabriel

    ```SQL
    
    ```
