# 1089. Duplicate Zeros

# Solution1: get a tmp array
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # get a tmp array 
        if not arr: return arr
        tmp = []
        for val in arr:
            if len(tmp) < len(arr):
                if val == 0:
                    tmp.extend([0, 0])
                else:
                    tmp.append(val)
        for i in range(len(arr)):
            arr[i] = tmp[i]

# Solution2: start from back to modify the array
    # count nuimber of 0 to get number of shift
    # start the right to left -> the current index + shift => thre final place
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        for i in range(len(arr)-1, -1, -1):
            # the order here matters
            if i + zeros < len(arr):
                arr[i+zeros] = arr[i]
                
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < len(arr):
                    arr[i+zeros] = 0
