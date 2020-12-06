# Feedbacks:
# right pointer can be len() or len() - 1
# right/left pointer can do right = mid -1 or right = mid given by the while condition
# while left <= right: then right = mid - 1, left = mid + 1 because left and right index can be on the same index and get all element search
# while left < right: then means there always one element will not be searched, have to use use right = mid
# when use len() then must right < left : otherwise will index of out bounds
# when use len() - 1, okay to use both left <= right / left < right

def search(nums, target):
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
print(search([1, 3], 1))