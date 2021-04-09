class Solution1:
    def mergeSort1(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.mergeSort1(nums[:mid])
        right = self.mergeSort1(nums[mid:])
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                nums[k] = right[j]
                j += 1
            else:
                nums[k] = left[i]
                i += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            nums[k] = right[j]
            k += 1
            j += 1
        return nums


class Solution2:
    def mergeSort(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(nums, left, right)

    def merge(self, nums, left, right):
        i, j, k = 0, 0, 0
        tmp = []
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                # nums[k] = right[j]
                tmp.append(right[j])
                j += 1
            else:
                # nums[k] = left[i]
                tmp.append(left[i])
                i += 1
            # k += 1
        if i < len(left):
            tmp += left[i:]
        if j < len(right):
            tmp += right[j:]
        return tmp


if __name__ == "__main__":
    sol = Solution1()
    print(sol.mergeSort1(nums=[1]))
    print(sol.mergeSort1(nums=[2, 1]))
    print(sol.mergeSort1(nums=[22, 4, 1]))
    print(sol.mergeSort1(nums=[2, 4, 11]))
    print(sol.mergeSort1(nums=[2, 4, 1, 9, 12, 3, 77, 98]))

    sol = Solution2()
    print(sol.mergeSort(nums=[1]))
    print(sol.mergeSort(nums=[2, 1]))
    print(sol.mergeSort(nums=[22, 4, 1]))
    print(sol.mergeSort(nums=[2, 4, 11]))
    print(sol.mergeSort(nums=[2, 4, 1, 9, 12, 3, 77, 98]))
