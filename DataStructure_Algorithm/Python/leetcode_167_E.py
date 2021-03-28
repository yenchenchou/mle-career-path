# 167. Two Sum II - Input array is sorted

# two pointers 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            elif s < target:
                left += 1
            else:
                right -= 1
    #O(n), O(1)


# Solution2: hash map
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, val in enumerate(numbers):
            if target - val in dic:
                return [dic[target-val]+1, i+1]
            dic[val] = i
    #O(n), O(n)


# Solution3: Binary Search
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1