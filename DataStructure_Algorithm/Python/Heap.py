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