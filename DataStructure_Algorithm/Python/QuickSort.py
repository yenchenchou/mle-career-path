from random import randrange


class Solution:
    # randomly select an element as a pivot
    # move the pivot to the last position by swap
    # iterate through the array and if the number if smaller than the pivot
    # put to left side of the pivot and to the right if on the right
    # get the new index position for the pivot
    # do it repeatedly  -> this means the pivot will find a fix position in the array
    def quickSort(self, nums):
        self.hepler(nums, 0, len(nums) - 1)
        return nums

    def hepler(self, nums, start, end):
        if start >= end:
            return None
        pivotIndex = randrange(start, end + 1)
        newIndex = self.partition(nums, start, end, pivotIndex)
        self.hepler(nums, start, newIndex - 1)
        self.hepler(nums, newIndex + 1, end)

    def partition(self, nums, start, end, pivotIndex):
        nums[pivotIndex], nums[end] = nums[end], nums[pivotIndex]
        newIndex = start
        for i in range(start, end):
            if nums[i] < nums[end]:
                nums[newIndex], nums[i] = nums[i], nums[newIndex]
                newIndex += 1
        nums[newIndex], nums[end] = nums[end], nums[newIndex]
        return newIndex


# O(n^2) -> O(nlogn), O(logn)

if __name__ == "__main__":
    sol = Solution()
    print(sol.quickSort(nums=[1]))
    print(sol.quickSort(nums=[2, 1]))
    print(sol.quickSort(nums=[22, 4, 1]))
    print(sol.quickSort(nums=[2, 4, 11]))
    print(sol.quickSort(nums=[2, 4, 1, 9, 12, 3, 77, 98]))
