# Syntax and Tips Reminder
#### `COUNT`
1. `COUNT` does not include `NULL`. **Aggregate functions like COUNT and SUM always ignore NULLs**

#### `DISTINCT`
1. Remember to consider select distinct and everything that may need to consider distinct

#### `Matching words`
1. wild cards: %, _, -, [], ^

#### `UNION`
1. UNION only appends distinct values. Which means not only union only keeps one distinct value after you combine the 
table but also each of you table will remain only distinct value

#### `WHERE`
1. When using `WHERE`, `NULL` value will be exclude by default. Remember to use `WHERE XXX OR <feature> IS NULL`

#### `WHERE` + `GROUP BY`
1. Using group by + where is okay, it's just the order where(condition on single row) -> groupb y -> having 
    (condition on group)

#### `SUBSTRING`(str FROM pos FOR len)
1. The forms without a len argument return a substring from string str starting at position pos. The forms with a len argument return a substring len characters long from string str, starting at position pos. The forms that use FROM are standard SQL syntax. It is also possible to use a negative value for pos. In this case, the beginning of the substring is pos characters from the end of the string, rather than the beginning. A negative value may be used for pos in any of the forms of this function. A value of 0 for pos returns an empty string.

#### `Time and Timestamp`
Date and time values can be represented in several formats, such as quoted strings or as numbers, depending on the exact
 type of the value and other factors. For example, in contexts where MySQL expects a date, it interprets any of 
 '2015-07-21', '20150721', and 20150721 as a date. [Reference to MySQL](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-literals.html)

* String and Numeric Literals in Date and Time Context.  MySQL recognizes DATE values in these formats:

    1. As a string in either 'YYYY-MM-DD' or 'YY-MM-DD' format. A “relaxed” syntax is permitted: Any punctuation character 
    may be used as the delimiter between date parts. For example, '2012-12-31', '2012/12/31', '2012^12^31', and '2012@12@31' 
    are equivalent.
    
    2. As a string with no delimiters in either 'YYYYMMDD' or 'YYMMDD' format, provided that the string makes sense as a 
    date. For example, '20070523' and '070523' are interpreted as '2007-05-23', but '071332' is illegal (it has nonsensical 
    month and day parts) and becomes '0000-00-00'.

    3. As a number in either YYYYMMDD or YYMMDD format, provided that the number makes sense as a date. For example, 
    19830905 and 830905 are interpreted as '1983-09-05'.

* MySQL recognizes DATETIME and TIMESTAMP values in these formats:

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

* Usual time operations
    * `DAY` = `DAY_OF_MONTH`
    * `DAYOFWEEK(date)`
    * `DAYOFYEAR(date)`
    * `EXTRACT(unit FROM date)`
    * `TO_DAYS(date)`: returns a day number (the number of days since year 0).
    * `TIMESTAMPDIFF(unit,datetime_expr1,datetime_expr2)`:  `MONTH`, `YEAR`, `MINUTE` ...
    *  `DATEDIFF`, `TIMEDIFF`
    * Resource: [12.7 Date and Time Functions](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_to-days):

* **Difference between datetime and timestamp**

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