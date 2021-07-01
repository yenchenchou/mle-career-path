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
    (3/9/2021, 3/23/2021, 8/11/2020, 4/17/2021, 8/27/2020)

        ```Python
        class Solution:
            def fillNa(self, string):
                if not string: return string
                cache = None
                for i, val in enumerate(string):
                    if val:
                        cache = val
                    if not val:
                        string[i] = cache
                return string

        sol = Solution()
        print(sol.fillNa([2, 3, None, 9]))
        print(sol.fillNa([None, 3, None, 9]))
        print(sol.fillNa([None, None, None, 9]))
        print(sol.fillNa([5,None,None, 1]))
        print(sol.fillNa([None]))
        print(sol.fillNa([]))

        # Avanced, fill the None by previous value, if not, use the later value
        if not string or len(string) == 1: return string
        for val in string:
            if val:
                start = val
                break

        for ind, ele in enumerate(string):
            if not ele:
                string[ind] = start
            else:
                start = ele
            
        return string
        ```

    2. Given a dictionary, print the key for nth highest value present in the dict.(4/17/2021)

        ```Python
        # Facebook
        dic = {'a': 1, 'b': 2, 'c': 100, 'd': 30}
        n = 2

        def solver(dic, n):
            
            dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
            if len(dic) == 1: return [dic[0][0]]
            res = [dic[0][0]]
            maxNum = dic[0][1]
            for key, val in dic[1:]:
                if val == maxNum:
                    res.append(val)
            return res
            # vals = sorted(dic.items(), key=lambda x: x[1], reverse=True)
            #return vals[n-1][0]

        # Advanced
        # Please refer to 347. Top K Frequent Elements
        ```

    3. Given two sentences, you have to print the words those are not present in either of the sentences. Use set, [see set operations](https://realpython.com/python-sets/). (3/23/2021, 9/11/2020, 8/11/2020, 4/17/2021)

        ```Python
        # use set
        def diff_words(a, b):

            if not a and not b:
                return []
            elif not a or not b:
                return a.split() if a else b.split()
            else:
                return list(set(a.split(" ")) ^ set(b.split(" ")))
                # return list(set(a.split(" ")).symmetric_difference(set(b.split(" "))))
        # symmetric_difference
        print(diff_words("HOW ARE you", "How are you"))
        print(diff_words("HOW ARE you", ""))
        print(diff_words("", ""))
        ```

    4. find s in missisipi -> Count Chars (8/11/2020, 4/17/2021, 8/27/2020)

        ```Python
        from collections import Counter
        def find_occur(input_val, word):
        #     cnt = Counter(input_val)
        #     print(cnt[word])
            if not input_val: return 0
            dic = {}
            for char in input_val:
                if char not in dic:
                    dic[char] = 1
                else:
                    dic[char] += 1
            return dic[word]

        find_occur('missisipi', 's')


        def find_occur(a='missisipi', b='s'):
            if not a: return 0
            cnt = 0
            for val in a:
                if val == b:
                    cnt += 1
            print(cnt)
        ```

    5. Balance the array: Given an array with n elements provide a dictionary of all teh needed elements to balance the array as keys of that dictionary and number of repeated occurraences of each of those elements that are required to balance the given array as values. Balance array would be an array containing all elements that appear equal number of times (8/27/2020)

        ```Python
        from collections import Counter
        class Solution:
            def findBalance(self, ls):
                if not ls: return dict()
                        
                dic = {}
                for val in ls:
                    if val and val not in dic:
                        dic[val] = 1
                    elif val and val in dic:
                        dic[val] += 1
                
                if dic:
                    cnt = sorted(dic.items(), key=lambda x: x[1])[-1][1]
                
                for key, val in dic.items():
                    dic[key] = cnt - val
                    
                return dic

        sol = Solution()
        print(sol.findBalance([4, 5, 11, 5, 6, 11, 11]))
        print(sol.findBalance([4, 11, 11]))
        print(sol.findBalance([11, 11]))
        print(sol.findBalance([None, 11]))
        print(sol.findBalance([None]))
        print(sol.findBalance([]))
        ```

    6. Complete a function that returns the smallest key(sorted in ascending order alphabetically) of the given input dictionary containing nth highest value dictionary: {'a': 1, 'b': 2, 'c': 100, 'd': 30}, n : 2 (2nd highest value) -> output: 'd'

        ```Python
        class Solution:
            def minK(self, dic, n):
                if not dic or len(dic) < n: return None
                dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
                return dic[n-1][0]

        sol = Solution()
        print(sol.minK({'a': 1, 'b': 2, 'c': 100, 'd': 30}, 2))
        print(sol.minK({'a': 1, 'b': 2, 'c': 2, 'd': 30}, 2))
        print(sol.minK({'a': 1}, 2))
        print(sol.minK({'a': 1, "b":4}, 3))
        ```

    7. Average length in a string (3/23/2020)

        ```python
        # Average length in a string
        class Solution:
            def func(self, t):
                if not t: return t
                length = 0
                for ele in t:
                    if ele:
                        for val in ele:
                            length += 1
                        
                return length/len(t)

        sol = Solution()
        print(sol.func(['avc','abcd','a','bbcc']))
        print(sol.func([None, 'd', 'bc']))
        print(sol.func(['', 'd', 'bc']))
        print(sol.func([None]))
        print(sol.func([]))
        ```

    8. Find string with most frequent (04/11/2020)

        ```Python
        from collections import Counter
        class Solution:
            def mostFreq(self, string):
                
                
                # By alphabical order
                if not string: return ""
                dic = {}
                for val in string:
                    if val not in dic:
                        dic[val] = 1
                    else:
                        dic[val] += 1
                dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
                return dic[0][0]
            
                # Any 
                return Counter(string).most_common(1)[0][0] if string else None
                
                # print if most counts are equal
                if not string: return []
                dic = {}
                for val in string:
                    if val not in dic:
                        dic[val] = 1
                    else:
                        dic[val] += 1
                    
                dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
                maxNum = dic[0][1]
                res = [dic[0][0]]
                for key, val in dic[1:]:
                    if val == maxNum:
                        res.append(key)
                return res
            
        sol = Solution()
        print(sol.mostFreq("iiiiiiintel"))
        print(sol.mostFreq("iiinnntel"))
        print(sol.mostFreq("i"))
        print(sol.mostFreq("ii"))
        print(sol.mostFreq(""))
        print(sol.mostFreq("ssddaa"))


        from collections import Counter
        class Solution:
            def mostFreq(self, string):
                if not string: return string
                cnt = Counter(string)
                maxVal = None
                res = []
                for key, val in cnt.items():
                    if not maxVal: 
                        maxVal = val
                        res.append(key)
                        continue
                    if maxVal == val :
                        res.append(key)
                return res
            
            
        sol = Solution()
        print(sol.mostFreq("iiiiiiintel"))
        print(sol.mostFreq("iiinnntel"))
        print(sol.mostFreq("i"))
        print(sol.mostFreq("ii"))
        print(sol.mostFreq(""))
        print(sol.mostFreq("ssdd"))
        print(sol.mostFreq(None))
        ```

    9. Return Boolean of IP the first component of the IP address contains 255 (04/11/2020)

        ```Python
        # Return Boolean of IP the first component of the IP address contains 255
        class Solution:
            def validIP(self, string):
                # Sol1
                return string.startswith("225") if string else False

                # Sol2
                return string.split(".")[0] == "225" if string else False

                
                
        sol = Solution()
        print(sol.validIP("225.23.12.41"))
        print(sol.validIP("25.23.12.41"))
        print(sol.validIP("222.23.123.41"))
        print(sol.validIP(""))
        ```

    10. sliding window
        - 219 Contains Duplicate II
        - 643 Maximum Average Subarray I

- Database
    1. Design ETL (12/21/2020)
    2. Data modeling (12/21/2020, 11/15/2020)

- SQL

    ```sql
    # The promotion datatset

    -- sales [product_id, customer_id, promotion_id, store_sales, transaction_date]
    -- products [product_id, product_class_id, product_name, is_low_fat_flg,  is_recyclable_flg]
    -- promotions [promotion_id, promotion_name, promotion_name, media_type, start_date, end_date]
    ```

    1. Top 5 (transaction/sales) single-channel media type (top 5 media type，这题是要看你的debug，最后要filter掉原来的multi media的channel，面试官会提示, use like '%single channel%') (4/17/2021) -> The promotion datatset

        ```sql
        select 

        ```

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

    6. The sales ratio between unpromoted sales and promoted sales

        ```SQL
        select 
        round(sum(case when s.transaction_date not between p.start_date and p.end_date then s.store_sales else 0 end)::decimal / sum(case when s.transaction_date between p.start_date and p.end_date then s.store_sales else 0 end)::decimal*100, 2) ratio
        from sales s
        left join promotions p
        on s.promotion_id = p.promotion_id

        -- exmaple 2
        with a as (
        select sum(store_sales) as revenue
        from sales a
            left join promotions b
            on a.promotion_id = b.promotion_id
        where a.transaction_date not between b.start_date and b.end_date
        ), b as (
        select sum(store_sales) as revenue
        from sales a
            left join promotions b
            on a.promotion_id = b.promotion_id
        where a.transaction_date between b.start_date and b.end_date
        )
        select 
        round((select revenue from a)::decimal / (select revenue from b)*100, 1) as per
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

    10. the (sales ratio, transaction ratio, and product)ratio between promotion units and non promotion (left join)

        ```sql

        ```

    11. Get the ratio of solf units and non-sold units from every product categories.

        ```sql
        ```

    12. Calculate average message amount by each country on each day from the users.

    13 [post success](https://www.interviewquery.com/questions/post-success)

        ```sql
        SELECT 
            DATE(c1.created_at) AS dt,
            avg(case when c2.user_id is not null then 1 else 0 end) AS post_success_rate
        FROM events AS c1
        LEFT JOIN events AS c2
            ON c1.user_id = c2.user_id
                AND c2.action = 'post_submit'
                AND DATE(c1.created_at) = DATE(c2.created_at)
        WHERE c1.action = 'post_enter'
            and c1.created_at between '2020-01-01' and '2020-01-31'
        GROUP BY 1
        ```

- Resource
  - [The Facebook Data Engineer Interview](https://towardsdatascience.com/the-facebook-data-engineer-interview-345235afaac0)

### Onsite/VO Questions

product sense：一开始还挺担心的，毕竟这种open ended的问题也不知道是不是对。准备的时候看了很多PM interview的mock视频，也看了几个medium的post之类的，大致了解了回答的框架，然后在准备的时候就根据这个框架来答题。因为并不是真的PM面试，所以可以主要集中在考虑相关的metrics上面
ETL：sql的难度没有很大，主要都是基础的join和计算，感觉如果过了phone screen对于sql来说问题不大
data modeling：用star schema可以解，面试官可以会引导你想出需要的metrics和dimension之类的
coding：之前也有担心过python coding，但是其实难度和phone screen差不多，也都是list和dictionary的一些基本loop之类的。地里可以在以前的面筋里面找到原题，如果没有信心的话可以找出来自己写写看，应该八九不离十
BQ：其实也不知道BQ回答得到底如何，但是基本也都是常规的BQ问题，可以在准备的时候想想用什么例子之类的

SQL：sales promotion product 的表。
low fat和recyable的比例，记得换成float并且乘100
top 5 media type，这题是要看你的debug，最后要filter掉原来的multi media的channel，面试官会提示
sale在promotion第一天或者最后一天的比例，case when可以解
有promotion的units和没有promotion的units 的ratio，这里要用left join
做得太快还被加了一道SQL，最后没完全写出来就去做python了但是大致思路是对的，category里面有units sold和完全没有units sold的ratio

sql : 三张表 people ( pid, companyid, pname..), company(cid, loc_id, cname...) , location(loc_id, lname..)
找出company最多的location， 该location对应的company里的people， 返回 people name， company name

## Data Scientist

## Machine Learning Engineer / Software Engineer, Machine learning
