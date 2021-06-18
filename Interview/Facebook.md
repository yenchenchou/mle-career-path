# Interview Questions Summary

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

## Data Engineer / Software Engineer, Data

### Process

1. Phone interview: python & SQL concept
2. Phone interview with coding: 5 Python + 5 SQL but no need to complete all. 4 for each is enough. It's about time and conre case handling.
3. onsite
    - Python
    - SQL
    - Project / Work
    - ETL
    - Data modeling

### Phone Screen Questions

- Python
    1. Replace None value with previous value present in a list.
    (3/9/2021, 3/23/2021, 9/11/2021, 8/11/2020, 4/17/2021)

        ```Python
        ls = [2, 3, None, 9], [None, 3, None, 9], [None, None, None, 9], [5,None,None, 1], [None]
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

    2. Given a dictionary, print the key for nth highest value present in the dict.(4/17/2021)

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

    3. Given two sentences, you have to print the words those are not present in either of the sentences. Use set, [see set operations](https://realpython.com/python-sets/). (3/23/2021, 9/11/2020, 8/11/2020, 4/17/2021)

        ```Python
        # use set
        def diff_words(a, b):
            return set(a.split(" ")) ^ set(b.split(" "))
        ```

    4. find s in missisipi -> Count Chars (8/11/2020, 4/17/2021)

        ```Python
        from collections import Counter
        def find_occur(input_val, word):
        #     cnt = Counter(input_val)
        #     print(cnt[word])
            dic = {}
            for char in input_val:
                if char not in dic:
                    dic[char] = 1
                else:
                    dic[char] += 1
            return dic[word]

        find_occur('missisipi', 's')
        ```

    5. Balance the array: Given an array with n elements provide a dictionary of all teh needed elements to balance the array as keys of that dictionary and number of repeated occurraences of each of those elements that are required to balance the given array as values. Balance array would be an array containing all elements that appear equal number of times

    ```Python
    ls = [4, 5, 11, 5, 6, 11, 11]
    def findBalance(ls):
        if not ls: return ls
        dic = {}
        for val in ls:
            if val not in dic:
                dic[val] = 1
            else:
                dic[val] += 1
        # Then get max freq
        maxFreq = sorted(dic.items(), key=lambda x: -x[1])[0][1]
        res = dict()
        for key, val in dic.items():
            if val < maxFreq:
                res[key] = maxFreq - val
        return res
    ```

    6. sliding window

    7. category里面有units sold和完全没有units sold的ratio

- Database
    1. Design ETL (12/21/2020)
    2. Data modeling (12/21/2020, 11/15/2020)

- SQL

    ```
    # The promotion datatset

    <!-- sales [product_id, customer_id, promotion_id, store_sales, transaction_date] -->
    <!-- products [product_id, product_class_id, product_name, is_low_fat_flg,  is_recyclable_flg] -->
    <!-- promotions [promotion_id, promotion_name, promotion_name, media_type, start_date, end_date] -->
    ```

    1. Percentage (3/23/2021) -> The promotion datatset
    2. Find top 5 sales products having valid promotions (3/9/2020) -> The promotion datatset

        ```SQL
        with valid_sales as (
        select b.product_name, sum(a.store_sales) sales
        from sales a
            left join products b on a.product_id = b.product_id
            left join promotions c on a.promotion_id = c.promotion_id
        where a.transaction_date between c.start_date and c.end_date
        group by 1
        order by 2 desc
        )

        select product_name
        from valid_sales
        limit 5
        ```

    3. From the sales that had a valid promotion, what % of transactions/sales occur on either the very first day or the very last day of a promotion campaign. (3/9/2020, 8/7/2020, 4/17/2021) -> The promotion datatset

        ```SQL
        -- % transactions
        select 
        -- round(avg(case when s.transaction_date in (p.start_date, p.end_date) then 1 else 0 end)*100, 2) percentage
        round(avg(case when s.transaction_date = p.start_date or s.transaction_date = p.end_date then 1 else 0 end)*100, 2) percentage
        from sales s
        left join promotions p
        on s.promotion_id = p.promotion_id
        where s.transaction_date between p.start_date and p.end_date

        -- % sales

        select 
        -- round(sum(case when s.transaction_date in (p.start_date, p.end_date) then s.store_sales else 0 end)::decimal / sum(s.store_sales) * 100, 2) percentage
        round(sum(case when s.transaction_date = p.start_date or s.transaction_date = p.end_date then s.store_sales else 0 end)::decimal / sum(s.store_sales) * 100, 2) percentage
        from sales s
        left join promotions p
        on s.promotion_id = p.promotion_id
        where s.transaction_date between p.start_date and p.end_date
        ```

    4. Percentage of valid promotion in sales -> The promotion datatset (**average， percentage，increate rate are IMPORTANT!**)

        ```SQL
        select 
        round(avg(case when s.transaction_date between p.start_date and p.end_date then 1 else 0 end)*100, 2) percentage
        from sales s
        left join promotions p
        on s.promotion_id = p.promotion_id
        ```

    5. What percent of all products in the grocery chain's catalog are both low fat and recyclable? (4/17/2021) -> The promotion datatset

        ```SQL
        
        select
            round(avg(case when is_low_fat_flg = 1 and is_recyclable_flg = 1 then 1 else 0 end)*100, 2) percentage 
        from products
        ```

    6. The ratio between unpromoted sales and promoted sales

        ```SQL
        ```

    7. [Acceptance Rate By Date](https://platform.stratascratch.com/coding-question?id=10285&python=), why not case when? Because the you may wait for the 'accepted' on diffent days. So self join will be the solution.

        ```SQL
        select
            a.date,
            count(b.user_id_receiver) / count(a.user_id_sender)::decimal as percentage_acceptance
        from (
            select user_id_sender, user_id_receiver, date
            from fb_friend_requests
            where action = 'sent') a
        left join
            (select user_id_sender, user_id_receiver, date
            from fb_friend_requests
            where action = 'accepted') b
            on a.user_id_sender = b.user_id_sender and a.user_id_receiver = b.user_id_receiver
        group by 1
        ```

    8. [Popularity of Hack](https://platform.stratascratch.com/coding-question?id=10061&python=)

        ```SQL
        -- location, avg_popularity
        select
            a.location,
            avg(b.popularity) as avg_popularity
        from facebook_employees a
        join facebook_hack_survey b
            on a.id = b.employee_id
        group by 1
        ```

    9. [Search Ranking](https://www.interviewquery.com/questions/search-ranking):  Write a query to get the percentage of search queries where all of the ratings for the query results are less than a rating of 3. Please round your answer to two decimal points.

        ```SQL
        WITH low_rating AS (
            SELECT query
            FROM search_results
            -- solution 2
            -- where rating < 3
            GROUP BY 1
            HAVING SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) = COUNT(*)
            -- solution 3
            -- having max(rating) < 3
        ) 

        SELECT ROUND(COUNT(DISTINCT lr.query)/COUNT(DISTINCT sr.query),2) AS percentage_less_than_3
        FROM search_results AS sr 
        LEFT JOIN low_rating AS lr 
            ON sr.query = lr.query
        ```

- Resource
  - [The Facebook Data Engineer Interview](https://towardsdatascience.com/the-facebook-data-engineer-interview-345235afaac0)

### Onsite/VO Questions

product sense：一开始还挺担心的，毕竟这种open ended的问题也不知道是不是对。准备的时候看了很多PM interview的mock视频，也看了几个medium的post之类的，大致了解了回答的框架，然后在准备的时候就根据这个框架来答题。因为并不是真的PM面试，所以可以主要集中在考虑相关的metrics上面
ETL：sql的难度没有很大，主要都是基础的join和计算，感觉如果过了phone screen对于sql来说问题不大
data modeling：用star schema可以解，面试官可以会引导你想出需要的metrics和dimension之类的
coding：之前也有担心过python coding，但是其实难度和phone screen差不多，也都是list和dictionary的一些基本loop之类的。地里可以在以前的面筋里面找到原题，如果没有信心的话可以找出来自己写写看，应该八九不离十
BQ：其实也不知道BQ回答得到底如何，但是基本也都是常规的BQ问题，可以在准备的时候想想用什么例子之类的

## Data Scientist

## Machine Learning Engineer / Software Engineer, Machine learning
