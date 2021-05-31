# Interview Questions Summary

## Learning Resources

- [The Ultimate Guide to SQL Interview Questions](https://www.interviewquery.com/blog-sql-interview-questions/)
- [The Facebook Data Engineer Interview](https://towardsdatascience.com/the-facebook-data-engineer-interview-345235afaac0)
- [Ace your data science interview](https://www.interviewquery.com/)
- [Customized for your next interview](https://www.interviewquery.com/pricing)

## Tips SUmmary from Above

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

## Data Engineer / Software Engineer, Data

- Python
    1. Replace None value with previous value present in a list.
    (3/9/2021, 3/23/2021, 9/11/2021, 8/11/2020)

        ```Python
        ls = [2, 3, None, 9]
        def func(ls):
            if not ls: return []
            cache = None
            for i in range(len(ls)):
                if ls[i]:
                    cache = ls[i]
                else:
                    ls[i] = cache
            print(ls)

        # Avanced, fill the None by previous value, if not, use the later value
        start = next(ele for ele in a if ele is not None)
        for ind, ele in enumerate(a):
            if ele is None:
                a[ind] = start
            else:
                start = ele
        print(a)
        ```

    2. Given a dictionary, print the key for nth highest value present in the dict.

        ```Python
        # Facebook
        dic = {'a': 1, 'b': 2, 'c': 100, 'd': 30}
        n = 2

        def solver(dic, n):
            vals = sorted(dic.items(), key=lambda x: x[1], reverse=True)
            return vals[n-1][0]

        # Advanced
        # Please refer to 347. Top K Frequent Elements
        ```

    3. Given two sentences, you have to print the words those are not present in either of the sentences. Use set, [see set operations](https://realpython.com/python-sets/). (3/23/2021, 9/11/2020, 8/11/2020)

        ```Python
        # use set
        def diff_words(a, b):
            return set(a.split(" ")) ^ set(b.split(" "))
        ```

    4. find s in missisipi -> Count Chars (8/11/2020)

        ```Python
        Use dict
        ```

- Database
    1. Design ETL (12/21/2020)
    2. Data modeling (12/21/2020, 11/15/2020)

- SQL
    1. Percentage (3/23/2021)
    2. Find top 5 sales products having promotions (3/9/2020)
    3. What %age of sales happened on first and last day of the promotion (3/9/2020, 8/7/2020)

- Resource
  - [The Facebook Data Engineer Interview](https://towardsdatascience.com/the-facebook-data-engineer-interview-345235afaac0)

## Data Scientist

## Machine Learning Engineer / Software Engineer, Machine learning
