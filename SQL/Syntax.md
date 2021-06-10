# Syntax and Tips Reminder

#### `Aggregation functions`

1. `COUNT(*) includes all null/non-null` values but slow. `COUNT(column)` does not include `NULL`. `COUNT(DISTINCT column)` only count the unique non-null values in the column. No **Aggregate functions like COUNT and SUM always ignore NULLs**

2. All functions ignore NULLs
3. Applications & Questions
    - Counting all rows

        ```SQL
        SELECT COUNT(*)
        FROM tutorial.aapl_historical_stock_price
        ```

    - Counting columns
    - Counting columns on specific data types
    - Calcuation on non-numeric: `SUM`, `AVG`; others work on numeric and non-numeric
    - How it ignore NULLs

    ```SQL
        # same answer below
        SELECT AVG(high)
        FROM tutorial.aapl_historical_stock_price
        WHERE high IS NOT NULL

        SELECT AVG(high)
        FROM tutorial.aapl_historical_stock_price
    ```

4. `COUNT(DISTINCT var)`: this is helpful when duplicates matters, such as count unique month. There will be 12 months at maximum.

#### Comparison Operators

[link](https://www.sisense.com/blog/sql-symbol-cheatsheet/)

#### `DISTINCT` and `DISTINCT ON`

1. Remember to consider select distinct and everything that may need to consider distinct
2. Distinct on mutliple columns are by defaul
3. `DISTINCT ON (column1), column2` will only keeps one row for each group of duplicates. Remember to use order by to make sure the result is steady. [See more here](https://www.postgresqltutorial.com/postgresql-select-distinct/)
4. Distinct with aggregation, for example, `COUNT DISTINCT` is acount
5. Common questions:
    - `DISTINCT` vs `DISTINCT ON`
    - `COUNT(DISTINCT column)` vs  `COUNT(column)`

#### `Matching words (Wildcards) and (NOT) LIKE/ILIKE`

1. wild cards: %, _, -, [], ^
    - `%`: any number characters
    - `_`: single character
    - `[]`
    - `()`
    - `^`
2. `LIKE` is case sensitive, while `ILIKE` is not

#### `JOIN`

1. When making joins, if you have duplicates on either one table, the duplicate result is going to carry over to your joined result if matched.
2. [SQL Joins Using WHERE or ON](https://mode.com/sql-tutorial/sql-joins-where-vs-on/). Usually you will use `WHERE` after the tables are joined. Also, only when you are using inner will the result between these two the same. This problem will be easily found when you have joining keys with different name. Details in link.
3. Join on multiple keys
4. Self joins
5. Questions:
    - self join
        - when idetify columns where you need to compare some columns that need to be compare, for example identify companies that received an investment from Great Britain following an investment from Japan.

#### `UNION` / `UNION ALL`

1. UNION only appends distinct values. Which means union will remove duplicates
2. `OUTER JOIN` == `LEFT JOIN` union `LEFT JOIN`
3. `UNION` only keep distinct values. `UNION ALL` will keep all. You'll likely use UNION ALL far more often than UNION. In this particular case, there are no duplicate rows, so UNION ALL will produce the same results.

#### `WHERE`

1. When using `WHERE`, `NULL` value will be exclude by default. Remember to use `WHERE XXX OR <feature> IS NULL`

#### `WHERE` + `GROUP BY`

1. Using group by + where is okay, it's just the order where(condition on single row) -> groupb y -> having
    (condition on group)

#### `HAVING`

1. Used with `GROUP BY` everytime. It is the "clean" way to filter a query that has been aggregated, but this is also commonly done using a subquery.

#### `CASE`

1. Conditional statement
2. Template:

    ```SQL
    CASE
        WHEN condition THEN res
        WHEN condition2 THEN res2
        [ELSE res3]
    END [AS new_col_name]
    ```

3. When using condition in case when, better to explicitly express instead of overlap even the result may be the same

    ```SQL
    -- case one --
    SELECT player_name,
        weight,
        CASE WHEN weight > 250 THEN 'over 250'
                WHEN weight > 200 THEN '201-250'
                WHEN weight > 175 THEN '176-200'
                ELSE '175 or under' END AS weight_group
    FROM benn.college_football_players

    -- better way --
    SELECT player_name,
        weight,
        CASE WHEN weight > 250 THEN 'over 250'
                WHEN weight > 200 AND weight <= 250 THEN '201-250'
                WHEN weight > 175 AND weight <= 200 THEN '176-200'
                ELSE '175 or under' END AS weight_group
    FROM benn.college_football_players

    ```

4. `CASE` helps to handle NULLs while you still want to use aggregation.
5. The data types of all the result expressions must be convertible to a single output type

#### `EXISTS`

1. Def: A boolean operator that tests for existence of rows in a subquery.
2. The column name in the subquery is not important, the important things are the columns and conditions you want to check in the subquery
3. [see detail](https://www.postgresqltutorial.com/postgresql-exists/)

#### `SUBSTRING`(str FROM pos FOR len)

1. The forms without a len argument return a substring from string str starting at position pos. The forms with a len argument return a substring len characters long from string str, starting at position pos. The forms that use FROM are standard SQL syntax. It is also possible to use a negative value for pos. In this case, the beginning of the substring is pos characters from the end of the string, rather than the beginning. A negative value may be used for pos in any of the forms of this function. A value of 0 for pos returns an empty string.

#### `CAST`

Convert a Value of One Type to Another

- Methods:
    1. `CAST(columns as DOUBLE/DATE/INTEGER/BOOLEAN/INTERVAL..etc)`
    2. Cast operator: `expression::type`
    3. [see deatil](https://www.postgresqltutorial.com/postgresql-cast/)

#### String functions

There are many string related functions for data cleaning

- `LEFT`, `RIGHT`, `SUBSTR` and `LENGTH`
- `TRIM`: remove characters from begginign and end of the string
- `POSITION` and `STRPOS`
- `CONCAT` / `||`
- `COALESCE`: The COALESCE function returns the first of its arguments that is not null. Null is returned only if all arguments are null. It is often used to substitute a default value for null values when data is retrieved for display, for example:

#### `Date/Time Functions`

Date time operations are tedious but essential. Usually, you will involve with the followings (We use postgres as examples here):

1. Convert different string to date/datetime/timestamp
    - common date/time functions, [see more](https://www.postgresql.org/docs/9.5/functions-datetime.html)
    - examples
        - current time: `current_time`, `current_date`, `current_timestamp` == `now()`, `localtime`, `localtimestamp`
        -convert
            - type one: `make_date`, `make_timestamp`, `make_time`, `make_timestamptz` -> `2013-07-15 08:15:23.5+01 (make_timestamptz)`/`2013-07-15 08:15:23.5 (make_timestamp)`
            - type two:
                - `cast('2020-02-01 15:10:10' as timestamp)`
                - `date '2020-02-01'` == `cast('2020-02-01' as date)` == `'2020-02-01'::date`. Apply for `TIME`, `DATE`, `TOMESTAMP`, ,`TOMESTAMPTZ`..etc. [see more](https://www.postgresql.org/docs/9.5/functions-datetime.html) and [data type formatting](https://www.postgresql.org/docs/8.4/functions-formatting.html)

2. Given date/datetime/timestamp, get the week, number of weeks..etc
    - Examples:
        - EXTRACT(field FROM source)
        - `SELECT EXTRACT(YEAR/QUARTER/MONTH/DAY FROM TIMESTAMP '2016-12-31 13:30:15');`
        - `SELECT EXTRACT(DAY FROM INTERVAL '6 years 5 months 4 days 3 hours 2 minutes 1 second' )`;
        - `YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, YEAR TO MONTH, DAY TO HOUR, DAY TO MINUTE, DAY TO SECOND, HOUR TO MINUTE, HOUR TO SECOND, MINUTE TO SECOND`
        - [see more](https://www.postgresqltutorial.com/postgresql-extract/)

3. Given date/datetime/timestamp, calculate the interval
    - Examples:
        - `date '2001-09-28' + integer '7'` -> date '2001-10-05'
        - `date '2001-09-28' + interval '1 hour'` -> timestamp '2001-09-28 01:00:00'
        - `timestamp '2001-09-28 01:00' + interval '23 hours'` -> timestamp '2001-09-29 00:00:00'
        - `21 * interval '1 day'` -> interval '21 days'
        - `age(timestamp, timestamp)` -> 43 years 9 mons 27 days
        - `timestamp` - `timestamp` -> interval '1 day 15:00:00' (days as unit)
        - [see more](https://www.postgresql.org/docs/9.5/functions-datetime.html)

4. `timestamp` vs timestamptz`: the difference between them is timestamptz includes time zone and support automatic time zone change according to your database server location.`timestamptz` use UTC by default. [See detail](https://www.postgresqltutorial.com/postgresql-timestamp/)

#### Subquery

Subquery can be used in different ways, using subquery behid `FROM` is most common. Several applications

1. FROM
2. Subqueries in conditional logic: functions like `WHERE`, `JOIN`/ON, `CASE` only accept subqueries that has only one-cell result. Only functions like `IN` can have multiple.
3. Joining subqueries
4. Subqueries and Uninion

#### `Window function`

1. **A window function performs a calculation across a set of table rows that are somehow related to the current row**.
This is comparable to the type of calculation that can be done with an aggregate function. But unlike regular
aggregate functions, use of a **window function does not cause rows to become grouped into a single output row — the
rows retain their separate identities(it works on the rows of the window frame rather than whole partition)**. Behind the scenes, the window function is able to access more than just the
current row of the query result. Adding `OVER` designates it as a window function Common combination: `SUM, AVG, COUNT, ROW_NUMER, RANK, DENSERANK, NTILE, LAG, LEAD`. [See more](https://mode.com/sql-tutorial/sql-window-functions/#the-usual-suspects-sum-count-and-avg)
    - SUM, AVG, COUNT: if the rows from `order by` hold the same value, then they will get the same value
    - ROW_NUMER
    - RANK: also affected by `order by`, ties are assigned if same ranked but will skip the next rank.
    - DESNE_RANK: also affected by `order by`, ties are assigned if same ranked but **will not** skip the next rank.
    - NTILE(integer)
    - LEAD(colum, integer), LAG(column, integer): will cause NULL if no previous/end of the row. You may take window function aprt as subquery and use the outer query to filter out the NULLs.

    ```SQL
    SELECT *
    FROM (
        SELECT start_terminal,
            duration_seconds,
            duration_seconds -LAG(duration_seconds, 1) OVER
                (PARTITION BY start_terminal ORDER BY duration_seconds)
                AS difference
        FROM tutorial.dc_bikeshare_q1_2012
        WHERE start_time < '2012-01-08'
        ORDER BY start_terminal, duration_seconds
        ) sub
    WHERE sub.difference IS NOT NULL
    ```

    ```SQL
    SELECT depname, empno, salary, enroll_date
    FROM
    (SELECT depname, empno, salary, enroll_date,
            rank() OVER (PARTITION BY depname ORDER BY salary DESC, empno) AS pos
        FROM empsalary
    ) AS ss
    WHERE pos < 3;
    ```

   1. [mode](https://mode.com/sql-tutorial/sql-window-functions/#ntile)
   2. [official website](https://www.postgresql.org/docs/9.1/tutorial-window.html)

#### `WITH`

WITH provides a way to write auxiliary statements for use in a larger query. These statements, which are often referred to as Common Table Expressions or CTEs, can be thought of as defining temporary tables that exist just for one query.

#### Column naming

1. If you insist to name your column such as `new column`, then use double qoute "new column"

## Tips for optimizing the databse

1. Higer Level

    - table size: use filters
    - Use limit to test query logic

    -

## Resource

1. [Mode Analytics](https://mode.com/sql-tutorial/)
