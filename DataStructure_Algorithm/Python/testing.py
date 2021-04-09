class Solution:
    def mergeSort(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(nums, left, right)
        
    def merge(self, nums, left, right):
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                nums[k] = right[j]
                j += 1
            else:
                nums[k] = left[i]
                i += 1
            k += 1
        if i < len(left):
            nums[k:] = left[i: len(left)]
        if j < len(right):
            nums[k:] = right[j: len(right)]
        return nums

if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeSort(nums=[1]))
    print(sol.mergeSort(nums=[2, 1]))
    print(sol.mergeSort(nums=[22, 4, 1]))
    print(sol.mergeSort(nums=[2, 4, 11]))
    print(sol.mergeSort(nums=[2, 4, 1, 9, 12, 3, 77, 98]))