# 11. Container With Most Water
# Solution1: Start from two pinters, one from start and the other from the end
# why start from farest pointers works? Need proof
# The area is decided by the width between bar locations and the heights
# So, under the situation we don't know the height, at least we may get bigger area by making them far
# Why moving the lower height towrds the middle works:
# [1,4,5,2,6]
# proof by contradiction: say you have two bars and you move the higher bar to the middle this time.
# You are shrinking the width and since the area is somehow dicides by the min height, which means your effective height is not changing
# Thus, moving the higher bar doesn't not benefit

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # the two bars will need to be as far as possible
        left, right = 0, len(height)-1
        area = 0
        while left < right:
            area = max(area, (right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return area
