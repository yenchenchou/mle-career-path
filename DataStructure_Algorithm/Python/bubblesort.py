# Implement bubble sort
# Solution1:
class Solution:
    def bubbleSort(self, nums):
        for j in range(0, len(nums)):
            for i in range(0, len(nums) - j - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums


# O(n^2)-> best case will be O(1) by the helped of swapped flag, O(1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.bubbleSort(nums=[1]))
    print(sol.bubbleSort(nums=[2, 1]))
    print(sol.bubbleSort(nums=[22, 4, 1]))
    print(sol.bubbleSort(nums=[2, 4, 11]))
    print(sol.bubbleSort(nums=[2, 4, 1, 9, 12, 3, 77, 98]))
