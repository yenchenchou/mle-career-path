# 1094. Car Pooling
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # overlapping problem -> stack -> remains
        # [[3,2,7],[8,3,9], [3,7,9]]
        stack = []
        for n, start, end in trips:
            stack.append([start, n])
            stack.append([end, -n])
        stack.sort()
        for los in stack:
            capacity -= los[1]
            if capacity < 0:
                return False
        return True  # O(nlogn), O(n)
