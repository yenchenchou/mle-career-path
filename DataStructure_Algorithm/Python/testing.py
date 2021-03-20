def findIndex(nums,left, right):
    if nums[left] < nums[right]:
        return 0

    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] > nums[pivot + 1]:
            return pivot + 1
        else:
            if nums[pivot] > nums[left]:
                left = pivot + 1
            else:
                right = pivot - 1

def find_rotate_index(nums, left, right):
    if nums[left] < nums[right]:
        return 0

    while left <= right:
        pivot = (left + right) // 2
        print(pivot)
        if nums[pivot] > nums[pivot + 1]:
            return pivot + 1
        else:
            if nums[pivot] < nums[left]:
                right = pivot - 1
            else:
                left = pivot + 1

# print(findIndex([4,5,0,1,2,3], 0, 5))
print(find_rotate_index([4,5,6,7,0,1,2,3], 0, 5))