def siftUp(nums, index):
    parentIndex = (index - 1) // 2
    if index < 0 or nums[index] > nums[parentIndex]:
        return
    nums[index], nums[parentIndex] = nums[parentIndex], nums[index]
    siftUp(nums, index)


arr = [0, 1, 5, 6, 8, -1]
siftUp(arr, len(arr) - 1)
print(arr)
