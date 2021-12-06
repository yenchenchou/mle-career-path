"""
Intro
1. To break the problem into small problems with size of half of the original problem
"""

# 1. Classic Binary Search
def classic_binary_search(nums, target):
    if not nums or len(nums) == 0: return -1
    left, right = 0, len(nums) - 1
    while left <= right:  # if the target equal to our only one element array, so we need =
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # +1 because we are sure that mid is not the target
        else:
            right = mid - 1
    return -1


# 2. Classic Binary Search in 2D array
def classic_binary_search_2d(nums, target):
    if not nums or len(nums) == 0 or len(nums[0]) == 0: return -1
    row, col = len(nums), len(nums[0])
    left, right = 0, row * col - 1
    while left <= right:
        mid = (left + right) // 2
        r, c = mid // col, mid % col
        if nums[r][c] == target:
            return mid
        elif nums[r][c] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# 3. closet to target number:
def closet_target_number(nums, target):
    """'
    1. NO need for exact number -> FIND the interval that include the target
    2. not sure whether the current value of left/right nunber is corrent -> need post processing
    3. stop at when left and right are neigbor -> because we are finding the interval
    """
    if not nums or len(nums) == 0: return -1
    left, right = 0, len(nums) - 1
    while left + 1 < right:  # if the target equal to our only one element array, so we need =
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid
    if abs(nums[left] - target) < abs(nums[right] - target):
        return left
    else:
        return right


# 4.1 return index of first occurance of an sorted non decreased array
def first_occurance(nums, target):
    """
    [1,2,2,2,2,3], t=2
     l         
       r  
    m
        
    1. will find the value but keep index as left as possible
    -> let the pointer compare the neghbor pointer to see which is current, the stop when left and right overlapped
        -> left pointer: move a step further +1 after mid
        -> right pointer: stop at where the mid point is since it is not the value

    -> Option2: let the pointer be neigbor then see which one is the first one
    """
    # Option1
    if not nums or len(nums) == 0: return -1
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid  # mid - 1 is not ok otherwise skip the value
        else:
            left = mid + 1  # mid is not ok otherwise infinite loop
    return left if nums[left] == target else -1

    # Option2: the pros for this is because it the structure is the same compare to the finding last occurence problem
    # if not nums or len(nums) == 0: return -1
    # left, right = 0, len(nums) - 1
    # while left + 1 < right:  # if the target equal to our only one element array, so we need =
    #     mid = (left + right) // 2
    #     if nums[mid] == target:
    #         right = mid
    #     elif nums[mid] < target:
    #         left = mid  # mid + 1 is ok
    #     else:
    #         right = mid # mid - 1 is ok
    # if nums[left] == target:
    #     return left
    # elif nums[right] == target:
    #     return right
    # else:
    #     return -1

# assert first_occurance([1,2,2,2,2,3], target=2) == 1
# assert first_occurance([2,2,2,2], target=2) == 0
# assert first_occurance([1,2,3], target=2) == 1
# assert first_occurance([1,2,2,2,2,3], target=3) == 5
# assert first_occurance([], target=2) == -1
# assert first_occurance([1,3], target=10) == -1


# 4.2 return index of last occurance of an sorted non decreased array
# def last_occurance(nums, target):
#     """
#     [1,2,2,2], t=2
#            r
#          m
#          l 
#     """
#     if not nums or len(nums) == 0: return -1
#     left, right = 0, len(nums) - 1
#     while left + 1 < right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             left = mid
#         elif nums[mid] > target:
#             right = mid  # both mid - 1 is ok because we are sure the current value is not the target
#         else:
#             left = mid  # both mid + 1 is ok because we are sure the current value is not the target
#     if nums[right] == target:
#         return right
#     elif nums[left] == target:
#         return left
#     else:
#         return -1
# assert last_occurance([1,2,2,2,2,3], target=2) == 4
# assert last_occurance([2,2,2,2], target=2) == 3
# assert last_occurance([1,2,3], target=2) == 1
# assert last_occurance([1,2,2,2,2,3], target=3) == 5
# assert last_occurance([], target=2) == -1
# assert last_occurance([1,3], target=10) == -1

# 5. How to find k elements closest to target number in a ascending array
def find_k_closest_to_target(nums, target, k):
    """
    1. sliding window like problem with fix size window
     -> find closest with O(logn) and expand left/right from the closest value O(k)
     -> move the pointer left if the left one is closer, vise versa
    """
    mid = closet_target_number(nums, target)
    left, right = mid, mid
    
    while right - left < k:
        if left == 0:
            return nums[:k]
        elif right == len(nums):
            return nums[-k:]
        else:
            # move if difference is smaller and beware of the array range limit
            if target - nums[left-1] <= nums[right] - target:
                left -= 1
            else:
                right += 1
    return nums[left: right]
                
assert find_k_closest_to_target([1,2,2,3,4,5], target=2, k=3) == [1,2,2]
assert find_k_closest_to_target([1,2,2,3,5,6], target=2, k=4) == [1,2,2,3]
assert find_k_closest_to_target([1,2,2,3,5,6], target=1, k=3) == [1,2,2]
assert find_k_closest_to_target([1,1,1,10,10,10], target=9, k=1) == [10]
assert find_k_closest_to_target([1,1,1,10,10,10], target=9, k=4) == [1,10,10,10]
