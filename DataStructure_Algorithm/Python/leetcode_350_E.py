# 350. Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # choose one save in dic and count, then iterate the other one        
        # use set
        dic, res = {}, []
        for val in nums1:
            if val not in dic:
                dic[val] = 1
            else:
                dic[val] += 1
        for val in nums2:
            if val in dic and dic[val] > 0:
                dic[val] -= 1
                res.append(val)
        return res
    # O(n+m), O(n)

# Follow-up Questions
# What if the given array is already sorted? How would you optimize your algorithm?

# We can use either Approach 2 or Approach 3, dropping the sort of course. It will give us linear time and constant memory complexity.
# What if nums1's size is small compared to nums2's size? Which algorithm is better?

# Approach 1 is a good choice here as we use a hash map for the smaller array.
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# If nums1 fits into the memory, we can use Approach 1 to collect counts for nums1 into a hash map. Then, we can sequentially load and process nums2.

# If neither of the arrays fit into the memory, we can apply some partial processing strategies:

# Split the numeric range into subranges that fits into the memory. Modify Approach 1 to collect counts only within a given subrange, and call the method multiple times (for each subrange).

# Use an external sort for both arrays. Modify Approach 2 to load and process arrays sequentially.

