class Solution:
    def selectionSort(self, nums):
        for i in range(len(nums) - 1):
            minIndex = i
            for j in range(i + 1, len(nums)):
                if nums[minIndex] > nums[j]:
                    minIndex = j
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
        return nums


# O(n^2), O(1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.selectionSort(nums=[1]))
    print(sol.selectionSort(nums=[2, 1]))
    print(sol.selectionSort(nums=[22, 4, 1]))
    print(sol.selectionSort(nums=[2, 4, 11]))
    print(sol.selectionSort(nums=[2, 4, 1, 9, 12, 3, 77, 98]))
