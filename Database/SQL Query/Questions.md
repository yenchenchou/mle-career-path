# Questions and Answers

## Learning Resources

- [The Ultimate Guide to SQL Interview Questions](https://www.interviewquery.com/blog-sql-interview-questions/)
- [The Facebook Data Engineer Interview](https://towardsdatascience.com/the-facebook-data-engineer-interview-345235afaac0)
- [Ace your data science interview](https://www.interviewquery.com/)
- [Customized for your next interview](https://www.interviewquery.com/pricing)

## Tips Summary from Above

- Strategies for the live SQL interview
  - Repeat the problem statement
  - Understand the edge cases (Do duplicate events matter? Are we looking at distinct users?)
  - Try working backwards if the problem is tricky
  - Pattern match to different functions
  - Practice
- The 7 different SQL interview questions
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

### When to use coalesce

1. n th highest/lowest value: `coalesce((select * ...))`

    ```SQL
    -- Write your MySQL query statement below
    -- not very generalized
    -- when the question does not require you to return NULL
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

    -- 2. Better way
    -- when the question does require you to return NULL
    select
        coalesce((
            select distinct salary as SecondHighestSalary 
            from employee
            order by 1
            limit 1
            offset n-1
        ))  as SecondHighestSalary
    ```

### When to use case when

1. Getting percentage from a column that numerator has stricter condition and the denominator with the looser condition. Usually questions involve **ration/percentage**
    - Tricks
        - When you know you need to use the same data set with the same column. Then it means you need to do self (left) join then do case when
    - For exmaple:
        - From the sales that had a valid promotion, what % of transactions/sales occur on either the very first day or the very last day of a promotion campaign.
        - Percentage of valid promotion in sales
        - You're given a table that contains search results. If the 'position' column represents the position of the search results, write a query to calculate the percentage of search results that were in the top 3 position.
        - Write a query to calculate the percentage of search results, out of all the results, that were positioned in the top 3 and clicked by the user.
        - What percent of all products in the grocery chain's catalog are both low fat and recyclable?
        - Acceptance Rate

2. Filter on a column with multiple possible values
    - Customers Who Bought Products A and B but Not C: use case when to create tmp table first.

        ```sql
        with tmp as (
            select
                customer_id,
                sum(case when product_name = 'A' then 1 else 0 end) as prod_a,
                sum(case when product_name = 'B' then 1 else 0 end) as prod_b,
                sum(case when product_name = 'C' then 1 else 0 end) as prod_c
            from orders
            group by 1
        )

        select *
        from customers a
        where exists (
            select 1
            from tmp b
            where a.customer_id = b.customer_id
                and b.prod_a > 0
                and b.prod_b > 0
                and b.prod_c = 0
        )
        ```

### When to use group by or distinct

1. Without aggregation: When you need distinct value but still need to filter something based on conditions
2. With aggregation

### When to use aggregation

1. Without `group by`: When only one output column, without addtional info from the aggregation.
    - get the max salary at 2020:

        ```SQL
        select max(salary) as salary 
        from employee_table 
        where year = 2020;
        ```

    - What if you want the employee name with max salary at 2020: use subquery, but usually you will just use group by. We need to do filtering using `where` beforehand that's why we can't use aggregation function right away/

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

2. With `group by`

    - When you need aggregated info along with other info, the most common one

        ```sql
        select id, avg(score)
        from employee_table
        group by 1
        ```

    - Filtering with aggregation, **You can use different aggregate function in HAVING Clause**: fetch all names from list which has average ammount of all their amounts greater than 150

        ```sql
        select month, round(avg(volume))
        from tutorial.aapl_historical_stock_price
        group by 1
        having count(volume) > 300 and avg(low) > 170
        order by 1
        ```

### When to use EXIST/IN/JOIN

1. EXISTS: When you just want the columns from one table but need filters/conditions from other tables. You can still use join but not efficient
    - Find customers who have at least one payment whose amount is greater than 11 [see details](https://www.postgresqltutorial.com/postgresql-exists/)

        ```SQL
        -- use exists
        select c.name
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

2. join
    - self join:
        - compare time lag on same value, check which id has higher temperature than previous day. self join applys even the order value is not consecutive. While, using `lead` or `lag` in window function in this question does not work if the datetime is not continuous
        - employee/manager/CEO comparison (manager is also an employee), [such as salary](https://leetcode.com/problems/employees-earning-more-than-their-managers/)

            ```sql
            select 
                a.name as employee
            from employee a
            join employee b
                on a.managerid = b.id
            where a.salary > b.salary
            ```

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
            ORD

        - find friends with conditions, such as ages bigger, id bigger..etc.
    - multiple joins: usually, we will use where to replace join for readability
        - [consecutive numbers check](https://leetcode.com/problems/consecutive-numbers/)

        - [1270. All People Report to the Given Manager, (multi similar column check)](https://leetcode.com/problems/all-people-report-to-the-given-manager/)

    - Multtple join condition
        - Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03".

            ```sql
            with tmp as (
                select
                    a.Request_at,
                    case when a.Status != 'completed' then 1 else 0 end as flag
                from trips a
                left join users b on a.Client_ID = b.users_id
                left join users c on a.driver_id = c.users_id
                where b.banned = 'No'
                    and c.banned = 'No'
                    and a.request_at between date '2013-10-01' and date '2013-10-03'
            )

            select Request_at as day, round(avg(flag), 2) as `Cancellation Rate`
            from tmp
            group by 1
            order by 1
            ```

    - left join
        - acceptance rate
            - Sol 1: `left join` then `count(a.accept)/count(b.request)`
            - Sol 2: `left join` then `avg(case when a.accept in not null then 1 else 0 end)`

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

### When to use Union or Union All

1. When having table with two columns that having the same meaning. Usaully envolve with people. For example, companies like facebook will ask Most Active Users On Messenger with table name `user1`, a message sender and `user2`, a message receiver. To know the total communicate count, you need union all.
    - An social network table that has `user1` and `user2`
        - `union`: You want to know total number of unique users.
        - `union all`: [Most Active Users On Messenger (either sender or receiver)](https://platform.stratascratch.com/coding-question?id=10295&python=)

### When to use window functions

1. Top k Salaries in each of the groups:
  top k salary/sales/friends means many units can have the same value. Usually `dense_rank()`. **Do not use other values like limit**

    ```sql
        -- 185. Department Top Three Salaries: dense rank
    with tmp as (
        select
            b.name as department,
            a.name as employee,
            a.salary,
            dense_rank() over(partition by a.departmentid order by a.salary desc) as ranker
        from employee a
        inner join department b
            on a.departmentid = b.id
    )
    select 
        department, employee, salary
    from tmp
    where ranker <= 3
    ```

2. Highest/lowest/top n/n th value of each group + **you need other info from the same table** + (may need info from other table). Or use subquery.

    ```sql
    -- window function
    with tmp as (
        select 
            name,
            salary,
            departmentid,
            dense_rank() over(partition by departmentid order by salary desc) as ranker
        from employee
    )

    select b.name as department, a.name as employee, a.salary
    from tmp a
    join department b
        on a.departmentid = b.id
    where ranker = 1

    -- subquery
    select d.Name as Department, e.Name as Employee, e.Salary
    from Employee as e
        join Department as d
        on e.DepartmentId = d.Id
        join (
            select max(Salary) as Salary, DepartmentId
            from Employee
            group by DepartmentId
        ) as mx
        on e.Salary = mx.Salary and e.DepartmentId = mx.DepartmentId;
    ```

3. include/exclude id that have both highest and lowest value in any of the group
    - [Find the Quiet Students in All Exams](https://leetcode.com/problems/find-the-quiet-students-in-all-exams/): use two window functions and do the include/exclude, then process the remainings.

        ```sql
        with tmp as (
            select 
                exam_id,
                student_id,
                rank() over(partition by exam_id order by score desc) as high_score,
                rank() over(partition by exam_id order by score) as low_score
            from exam
        ), tmp2 as (
            select student_id
            from tmp
            group by 1
            having (min(high_score) > 1 and min(low_score) > 1)
        )

        select distinct student_id, student_name
        from Student a
        where exists (
            select 1
            from tmp2 b
            where a.student_id = b.student_id
        )

        --sol2
        with tmp as (
            select
                *,
                dense_rank() over(partition by exam_id order by score) as low,
                dense_rank() over(partition by exam_id order by score desc) as high
            from exam
        ), tmp2 as (
            select
                student_id,
                max(case when low = 1 or high = 1 then 1 else 0 end) as not_quiet
            from tmp
            group by 1
        )

        select a.student_id, a.student_name
        from Student a
        where exists (
            select 1
            from tmp2
            where a.student_id = tmp2.student_id
                and tmp2.not_quiet = 0
        )
        ```

## Qestions by scenario

### Social Network

#### Example 1

```SQL
highschooler ('id', 'name', 'grade')
friend ('id1', 'id2')
likes ('id1', 'id2')
```

1. Find the names of all students who are friends with someone names Gabriel

    ```SQL
    
    ```

#### Example 2

```SQL
```
