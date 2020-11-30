# Comparison Note for efficient SQL

#### 1. Join vs Exists vs In
**`EXIST` works by looping each row of the outer table a time and check in the inner table, return true is 
exist; while `IN` get the all values from the inner table.** That's why outer big inner smaller user `IN` and use `EXIST` 
vise versa. Exists is a bit faster when two tables are equally sized.

Reading:

    1. [Join vs Exists vs In](http://www.gregreda.com/2013/06/03/join-vs-exists-vs-in/)
    2. [SQL中 join 、in 、exists 使用场景和执行效率](https://www.jianshu.com/p/c825c9bf42c2)
    3. [SQL 中的 EXISTS 到底做了什么？](https://zhuanlan.zhihu.com/p/20005249)