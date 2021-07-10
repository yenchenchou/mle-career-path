# 1299. Replace Elements with Greatest Element on Right Side

# Solution1: take max of the subarray from the right side of the current value
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # 3:49
        for i in range(len(arr) - 1):
            arr[i] = max(arr[i + 1 :])
        arr[-1] = -1
        return arr  # O(n^2), O(1)


# Solution2:
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1
        maxVal = arr[n]
        arr[n] = -1

        for i in range(n - 1, -1, -1):
            num = arr[i]
            arr[i] = maxVal
            maxVal = max(maxVal, num)

        return arr  # O(n), O(1)
