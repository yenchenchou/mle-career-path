# Interview Questions Summary

## Data Engineer / Software Engineer, Data

### GlassDoor

- Python
    1. Replace None value with previous value present in a list.
    (3/9/2021, 3/23/2021, 9/11/2021)

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
        ```

    2. Given a dictionary, print the key for nth highest value present in the dict.

        ```Python
        # Please refer to 347. Top K Frequent Elements
        ```

    3. Given two sentences, you have to print the words those are not present in either of the sentences. Use set, [see set operations](https://realpython.com/python-sets/). (3/23/2021, 9/11/2020)

        ```Python
        # use set
        def diff_words(a, b):
            return set(a.split(" ")) ^ set(b.split(" "))
        ```

    4. find s in missisipi -> Count Chars

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

## Data Scientist

## Machine Learning Engineer / Software Engineer, Machine learning
