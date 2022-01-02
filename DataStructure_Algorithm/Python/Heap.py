"""
Heap
A special tree-based data structure
"""
# 1. find smallest k elements from an unsorted array of size n (We need to ask the relationship between n and k)
## sol1: if n close to k then sort nlogn
## sol2: if k is relatively small then min heapify n and keep popping klogn -> n + klogn
### n + klogn
## sol3: max heap -> take k elements to heapify first, then for the remaining elements, if it's bigger then the top then pop the max heap and insert until all finish
### k + (n-k)logk
### sol 2 and sol3 depends 
#### if k is relitively small: min(n + logn)≈min(n), max(1 + nlogk)≈max(nlogk) -> depends
#### if k is relitively big (worst case is n/2 not n) then O(n/2 + nlogn)≈O(n/2 + nlogn) -> depends
# sol4: partially partition, the concept is from quick sort but not all process 


# Option1: binary search
    # Time: O(mlogn)
# Option2: two pointers
    # Time: O(m+n)
    # Space: O(1)
# Option3: hash table
    # shorter array to hash map to optimize space
    # for each element in longer array, check it with hashtable
    # Time: O(m+n)
    # Space: O(min(m, n))


# 1. because i is dynamic, so when we erase a char we need to let i -- to stay on the same position
# 2. erase is costly
# if the size if fixed, the unseen array will shfit to left and cause out of index error
"""
   sedkljwe
    i 
"""