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

#### `DISTINCT`

1. Remember to consider select distinct and everything that may need to consider distinct

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

1. UNION only appends distinct values. Which means not only union only keeps one distinct value after you combine the
table but also each of you table will remain only distinct value
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

#### `EXISTS`

1. Def: A boolean operator that tests for existence of rows in a subquery.
2. The column name in the subquery is not important, the important things are the columns and conditions you want to check in the subquery
3. [see detail](https://www.postgresqltutorial.com/postgresql-exists/)

#### `SUBSTRING`(str FROM pos FOR len)

1. The forms without a len argument return a substring from string str starting at position pos. The forms with a len argument return a substring len characters long from string str, starting at position pos. The forms that use FROM are standard SQL syntax. It is also possible to use a negative value for pos. In this case, the beginning of the substring is pos characters from the end of the string, rather than the beginning. A negative value may be used for pos in any of the forms of this function. A value of 0 for pos returns an empty string.

#### `Time and Timestamp`

Date and time values can be represented in several formats, such as quoted strings or as numbers, depending on the exact
 type of the value and other factors. For example, in contexts where MySQL expects a date, it interprets any of
 '2015-07-21', '20150721', and 20150721 as a date. [Reference to MySQL](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-literals.html)

- String and Numeric Literals in Date and Time Context.  MySQL recognizes DATE values in these formats:

    1. As a string in either 'YYYY-MM-DD' or 'YY-MM-DD' format. A “relaxed” syntax is permitted: Any punctuation character
    may be used as the delimiter between date parts. For example, '2012-12-31', '2012/12/31', '2012^12^31', and '2012@12@31'
    are equivalent.

    2. As a string with no delimiters in either 'YYYYMMDD' or 'YYMMDD' format, provided that the string makes sense as a
    date. For example, '20070523' and '070523' are interpreted as '2007-05-23', but '071332' is illegal (it has nonsensical
    month and day parts) and becomes '0000-00-00'.

    3. As a number in either YYYYMMDD or YYMMDD format, provided that the number makes sense as a date. For example,
    19830905 and 830905 are interpreted as '1983-09-05'.

- MySQL recognizes DATETIME and TIMESTAMP values in these formats:

    1. As a string in either 'YYYY-MM-DD hh:mm:ss' or 'YY-MM-DD hh:mm:ss' format. A “relaxed” syntax is permitted here,
    too: Any punctuation character may be used as the delimiter between date parts or time parts. For example,
    '2012-12-31 11:30:45', '2012^12^31 11+30+45', '2012/12/31 11*30*45', and '2012@12@31 11^30^45' are equivalent.
    The only delimiter recognized between a date and time part and a fractional seconds part is the decimal point.
    The date and time parts can be separated by T rather than a space. For example, '2012-12-31 11:30:45'
    '2012-12-31T11:30:45' are equivalent.

    2. As a string with no delimiters in either 'YYYYMMDDhhmmss' or 'YYMMDDhhmmss' format, provided that the string
    makes sense as a date. For example, '20070523091528' and '070523091528' are interpreted as '2007-05-23 09:15:28',
    but '071122129015' is illegal (it has a nonsensical minute part) and becomes '0000-00-00 00:00:00'.

    3. As a number in either YYYYMMDDhhmmss or YYMMDDhhmmss format, provided that the number makes sense as a date. For
    example, 19830905132800 and 830905132800 are interpreted as '1983-09-05 13:28:00'.

- Usual time operations
  - `DAY` = `DAY_OF_MONTH`
  - `DAYOFWEEK(date)`
  - `DAYOFYEAR(date)`
  - `EXTRACT(unit FROM date)`
  - `TO_DAYS(date)`: returns a day number (the number of days since year 0).
  - `TIMESTAMPDIFF(unit,datetime_expr1,datetime_expr2)`:  `MONTH`, `YEAR`, `MINUTE` ...
  - `DATEDIFF`, `TIMEDIFF`
  - Resource: [12.7 Date and Time Functions](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_to-days):

- **Difference between datetime and timestamp**

    0. A DATETIME stores a literal value of a date and time with no reference to any particular timezone. Whereas
    timestamp includes time zone. TIMESTAMP as taking the value you are setting and converting it from the current
    session time zone to UTC for storing and then converting it back to the current session time zone for displaying.
    That's why timestamp and datetime looks the same on the UI.

    1. [How timestamp store and display](https://stackoverflow.com/questions/39552135/timestamp-vs-datetime-mysql)

#### `Window function`

A window function performs a calculation across a set of table rows that are somehow related to the current row.
This is comparable to the type of calculation that can be done with an aggregate function. But unlike regular
aggregate functions, use of a window function does not cause rows to become grouped into a single output row — the
rows retain their separate identities. Behind the scenes, the window function is able to access more than just the
current row of the query result. Common combination: `SUM, AVG, COUNT, ROW_NUMER, RANK, DENSERANK, NTILE, LAG, LEAD`

   1. [mode](https://mode.com/sql-tutorial/sql-window-functions/#ntile)

#### `WITH`

Allows giving your sub-query block a name. You can do the following things
1.

#### Column naming

1. If you insist to name your column such as `new column`, then use double qoute "new column"

## Resource

1. [Mode Analytics](https://mode.com/sql-tutorial/)
