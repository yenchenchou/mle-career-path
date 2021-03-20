# Implement bubble sort
# Solution1:
class Solution:
    def bubbleSort(self, nums):
        for i in range(len(nums)-1):
            swapped = False
            for j in range(len(nums)-1-i):
                if nums[j] > nums[j+1]: 
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                print("no need to swap")
                return nums
        print("swapped previously")
        return nums
# O(n^2)-> best case will be O(1) by the helped of swapped flag, O(1)


if __name__=="__main__":
    sol = Solution()
    print(sol.bubbleSort(nums=[1]))
    print(sol.bubbleSort(nums=[2, 1]))
    print(sol.bubbleSort(nums=[22, 4, 1]))
    print(sol.bubbleSort(nums=[2, 4, 11]))
    print(sol.bubbleSort(nums=[2, 4, 1, 9, 12, 3, 77, 98]))