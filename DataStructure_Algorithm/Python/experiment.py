
# 1. Analyze the question 
# big picture: use the selection sort concept -> take the min value from unsorted array and put to the leftmost side of the unsorted array and do repeatly
# s1, s2 = place for unsorted, place for sorte
# global_min to record when we select the min when s1 to s2 and prevent from pushing back to s1
# when global_min == the value -> don't push back
# the s2 popping process stop when s2[-1] < global_min 
# clean up global_min
"""
4,2,1,5
s1 = [4,5]
s2 = [1,2]
global_min = None
"""
from typing import List

def twoStackSortNonDuplicates(nums) -> List:
    if not nums: return nums
    s1, s2 = nums, []
    
    for _ in range(len(nums)):
        global_min = float("inf")
        while s1: 
            val = s1.pop()  
            if val < global_min: 
                global_min = val # 4
            s2.append(val)  
        while s2:
            if s2[-1] < global_min: # 4, 4
                break
            val2 = s2.pop() #
            if val2 > global_min: 
                s1.append(val2)
        s2.append(global_min)
    return s2

assert twoStackSortNonDuplicates([4,1,5,2]) == [1,2,4,5], "should be [1,2,4,5]"
assert twoStackSortNonDuplicates([4,2]) == [2,4], "should be [2,4]"
assert twoStackSortNonDuplicates([1]) == [1], "should be [1]"
assert twoStackSortNonDuplicates([]) == [], "should be []"
# assert twoStackSortNonDuplicates([4,1,5,2,1,1]) == [1,1,1,2,4,5], "should be [1,1,1,2,4,5] but"