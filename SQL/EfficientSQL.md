# Comparison Note for efficient SQL

#### `JOIN` vs `EXISTS` vs `IN`
**`EXIST` works by looping each row of the outer table a time and check in the inner table, return true is 
exist; while `IN` get the all values from the inner table.** That's why outer big inner smaller user `IN` and use `EXIST` 
vise versa. Exists is a bit faster when two tables are equally sized.

   Reading:

   1. [Join vs Exists vs In](http://www.gregreda.com/2013/06/03/join-vs-exists-vs-in/)
  
   2. [SQL中 join 、in 、exists 使用场景和执行效率](https://www.jianshu.com/p/c825c9bf42c2)

   3. [SQL 中的 EXISTS 到底做了什么？](https://zhuanlan.zhihu.com/p/20005249)

#### Using `COUNT(*)`, `COUNT(1)`, and `COUNT(<feature>)`
1. `COUNT` is not only useful during group by, but also a way to avoid using subquery if used wisely. See example [1050. Actors and Directors Who Cooperated At Least Three Times](https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/). `COUNT(1)` does not refer to first column, instead, it is just a constant. The result of `COUNT(*)` and `COUNT(1)` are the same. Some documentation says `COUNT(1)` is optimized and thus quicker.
2. `COUNT` does not include `NULL`

   Reading:
      1. [Select Count(*) / Count(1) / Count(欄位名) 的差異
   ](https://dotblogs.com.tw/jeff-yeh/2011/01/12/20767)
   
#### Self join related
There are three common ways when using self join: 
1. `CROSS JOIN`: readable style
2. `FROM <table1> as a, <table1> as b WHERE a.x > b.x`: using `WHERE`
3. `select CAST(min(diff) as unsigned) as shortest from (
  select x - @prev as diff, @prev := x from point, (select @prev:=-100000000) tt order by x) t `