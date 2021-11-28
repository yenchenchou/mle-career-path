"""
As long as it follows the logic LIFO or FIFO, you can call them Stack or Queue. 
You can use array, list, or LinkedList ...etc to implement. Stack or Queue are just a concepts.

It's very rare to ask solely on Stack or Queue. It come with other data structures at the same time.

Common problems for Queue/Stack
1. Fix window size sliding window
2. Floating size sliding window
3. Use Stack implement Queue, Deque
"""
# 1. How to implement a queue by using two stacks(please describe it)


# 2. How to implement the min() function, when using 2 stacks or ine stack one hash map with time complexity
# follow up, minimize duplicate store in stack / hash map!!
# note that it's impossible to do that with one stack, so multiple stacks mix with other data structure is possible


# 3. Sort number with two stack, the input has no duplicates and all are int -> Use selection sort concept
# Follow up: if it has duplicte and the value is float
    # use a counter until counter minus to 0
def stack_sort(nums):
    # use the concept of selection sort: pick the min for unsorted to put to the leftmost of the sorted part
    # s1: unsorted values
    # s2: sorted value
    # cur_min: current min
    # idx = record who many pushed from cur_min

    # the input array push to s1 one by one
    # repeat until idx == len(input_array):
        # then pop + push from a1 to s2 one by one and record the min with the variable cur_min
        # then pop and push it back to s1 except for the value that matches the cur_min
        # push the cur_min to s2, and idx += 1
    s1, s2 = [nums], []
    cur_min = float("inf")
    while s1:
        val = s1.pop()
        if val < cur_min:
            cur_min = val # 1
        s2.append(val) # 4, 1, 3, 2
        while s2[-1] >= cur_min:
            s1.append(s2.pop())
        s2.append(cur_min)

        

        

            



# 4. How to use multiple stacks to implement a deque. Prefer O(1) amortized time for all operations
# three stack 

# When to use stack? When you need to look at the latest value of the left side 