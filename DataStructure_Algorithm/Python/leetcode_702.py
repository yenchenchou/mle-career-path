class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0
        
        left, right = 0, 1
        while reader.get(right) < target:
            right = right * 2
        
        while left <= right:
            pivot = left + (right - left) // 2
            num = reader.get(pivot)
            
            if num == target:
                return pivot
            elif num > target:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1

# the point is to set up the boundary and use binary search
# Time: O(logn), Space: O(1)