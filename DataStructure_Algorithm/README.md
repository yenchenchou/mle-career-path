# **Coding Path**

## **1. Sorting**

### **1.2 How to identify**

### **1.3 Common tricks in Binary search**

1. Quick Sort
2. Merge Sort
3. Selection Sort
4. Question summary
    * Basics:
        * the naive algorithm
    * Limited Stacks:
        * use 3 stacks to simulate selection sort
        * use 2 stacks to simulate selection sort
    * Linked List:
        * Merge sort linked list
        * Split the numbers and strings
    * Intervals:
        * #56. Merge Intervals
        * #253. Meeting Rooms II
        * #252. Meeting Rooms I

### **1.4 Common mistake points**

1. Sorting problems is not just from arrays or list, it can be any data structure that is sequential in some way.

---

1. Quick Sort:
    * Def: An algorithm that steps through each element in a sequence data structure. Then, compare the adjacent element and swap if it is not in a ascending/descending order.
    * Property: Each iteration, the largest/smallest element is sorted to the left most/right most side of the sequence.
    * Complexity:
        * Time: O(n^2)
        * Space: O(1)
2. Selection Sort:
    * Def: select the smallest element in an unsorted data structure and put it to the leftmost side of the unsorted section.
    * Property: work with other data structure at the same time
    * Complexity:
        * Time: O(n^2)
        * Space: O(1)
3. Merge Sort:
    * Def: Divide a sequential data structure from a certain point(usually mid point) repeatl until all the sub sections have one elements left. Then we pick the smaller one from the sub sections and merge the result repeatly until it is back to a sequential data structure
    * Property: The most used. Usually with recursion
    * Complexity:
        * Time: O(nlogn) <- O(logn+n)
        * Space: O(n) <- O(n/2+n/4+...1)
4. Quick Sort:
    * Def: Rnadomly select a point in an sequential data structure and call it a pivot. Then, put the values that smaller than the pivot to the left and bigger ones to the right.
    * Property:
        * Merge sort is a special case of quick sort.
        * Quick sort is an in-place sorting algorithm whereas Merge sort uses extra space.
        * The worst case runtime of quick sort is O(n^2) can be avoided by using randomized quicksort as explained in the previous point.
        * Quick Sort is also a cache friendly sorting algorithm as it has good locality of reference when used for arrays.
    * Complexity:
        * Time: O(n^2) but avg O(nlogn) since partitionw into two part then we only need logn layer * n elements
        * Space: O(n) but avg O(logn) since the heigth of stack

## **2. Binary Search**

---

### **2.1 Definition**

Binary Search operates on a contiguous sequence with a specified left and right index. The left, right, mid index helps us to compare the target. If the  index shows the condition deos not align with the target then that half part is eliminated. We do this repeatly then get the final result.

When solving binary search, there are several things included most of the time:

1. target: the target value you are searching for. Can be something around target
2. index: the current location that you are searching
3. left, right: the indices from which we use to maintain our search space
4. mid: the index used to apply a condition to determine if we should saerch left or right

Principles:

1. We must guarantee that the search space decreases over time
2. We must guarantee that the target cannot be ruled out accidentally

### **2.2 How to identify**

When you need to find one or more targets from a sorted sequence or a sequence need to be sorted

* Pre-processing - Sort if collection is unsorted.
* Binary Search - Using a loop or recursion to divide search space in half after each comparison.
* Post-processing - Determine viable candidates in the remaining space.

### **2.3 Common types and tricks in Binary search**

1. Type 1:
    * Search Condition can be determined without comparing to the element's neighbors (or use specific elements around it)
    * No post-processing required because at each step, you are checking to see if the element has been found. If you reach the end, then you know the element is not found
    * Usually will invloved `while left <= right`, `left = mid + 1`, `right = mid - 1`, terminate at `left > right`

2. Type 2:
    * An advanced way to implement Binary Search.
    * Search Condition needs to access element's immediate right neighbor
    * Use element's right neighbor to determine if condition is met and decide whether to go left or right
    * **Gurantees Search Space is at least 2 in size at each step (because left ,< right)**
    * Post-processing required. Loop/Recursion ends when you **have 1 element left**, such as `while left < right`. Need to assess if the remaining element meets the condition.
    * There is a chance that we need to examine right neignbor index

3. Type 3:
    * An alternative way to implement Binary Search
    * Search Condition needs to access element's immediate left and right neighbors
    * Use element's neighbors to determine if condition is met and decide whether to go left or right
    * Gurantees Search Space is at least 3 in size at each step
    * Post-processing required. Loop/Recursion ends when you have 2 elements left. Need to assess if the remaining elements meet the condition.

4. Other tricks or self summary
    * Check if `left <= right`, `left < right`, or `left < right - 1`
    * Compare with the target value or left most, right most, left neighbor, right neighbor
    * Whether skipping the mid is correct way
    * Becareful of index out of bound when point 1 is specified

5. Question summary
    * square root/pow/product related problems:
        * #69 Sqrt
        * #367 Valid Perfect Square
        * #50 Pow
    * First/last occurence:
        * #34. Find First and Last Position of Element in Sorted Array (two ways of thinking first/last)
    * Rotated:
        * #33. Search in Rotated Sorted Array
        * #153. Find Minimum in Rotated Sorted Array
        * #154. Find Minimum in Rotated Sorted Array II
    * Comparing left/right index in comparision, neighbor, return left/right index instead:
        * #35. Search Insert Position
        * #162. Find Peak Element
        * #278. First Bad Version
        * #162. Find Peak Element
    * Unknown size:
        * #702. Search in a Sorted Array of Unknown Size
    * Findclosest number:
        * #658. Find K Closest Elements
        * #270. Closest Binary Search Tree Value
    * Intersection:
        * #349 Intersection of Two Arrays  
        * #350 Intersection of Two Arrays II
    * Others:
        * #287 Find the Duplicate Number
        * #4 Median of two sorted array

### **2.4 Common mistake points**

## **3. LinkedList**

---

### **3.1 Definition**

A sequence data structure, the nodes are connected vis one or more links. Each node contains connections to other nodes in form of pointers. There are singly Linked List and double Linked List in general.

### **3.2 How to identify**

Linked List will be specified during the question

### **3.3 Common types and tricks in Linked List**

1. Type 1 - design linked list:
    *
2. Type 2 - cycle:
    * fast and slow pointer
3. Type 3 - reverse
    *
4. Type 4 - combine with common algorithms
    * mergesort a linked list
5. Type 5 -  Floyd's Tortoise and Hare
6. Question summary
    * design linked list:
        * #707 Design a Singly/Double LinkedList
        * #21: Merge Two Sorted
        * #203 Remove Linked List Elements
        * #19 Remove Nth Node From End of List
        * #328 Odd Even Linked
    * cycle / fast slow pointer
        * #141 Cycle in LinkedList
        * #142 LinkedList Cycle 2
        * #160 Intersection of Two Linked
    * reverse
        * #206 Reverse a LinkedList
        * #344 Reverse a string and swap the string in place(344 M): sentinel node concept, rescurion
        * #234 Palindrome Linked List
    * combine with common algorithms

### **3.4 Common mistake points**

1. When youde-reference a ListNode, make sure it is not a NUll pointer
2. Never lost conrol of the head pointer
3. Usually, we have no idea where is the head, we need a dummy node to handle that

## **Queue and Stack**

---

### **Recursion**

### **4.1 Definition**

### **4.2 How to identify**

### **4.3 ommon tricks in Recursion**

1. How to construct the recursion solution:
    * Base case (KNOWING WHEN TO SATOP!!)
    * What is will the recursive function looked like
    * what to return to pass the info to the next stack
    * which traverse order will benefit (pre-order, in-order, post-order)
2. When can we use:
    * When you can solve the question using functiona and solve it repeatly

### **4.4 Common mistake points**

---

### **5.1 Definition**

### **5.2 How to identify**

### **5.3 ommon tricks in Binary search**

### **5.4 Common mistake points**

---

## **Binary Tree**

### **6.1 Definition**

Binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child. Also, there are many special subtopics as well:

1. **Binary Search Tree**:

    Def: A node based binary tree with the following properties:

    1. The left subtree of a node should only contains node with keys smaller than the node's key
    2. The right subtree of a node should only contains nide with keys greater than the node's key
    3. The left and right subtree each must also be a binary search tree
    4. Some rare cases the right index doen't need to be len(arr)-1

2. **Full Binary Tree**

    Def: A node based biary tree  if every node has 0 or 2 children.

3. **Complete Binary Tree**

    Def: All nodes other than the last level has two children occupied. The nodes in the last layer are as far left as possible. A binary heap is a complete binary tree that satisfies the heap order prperty.

4. **Balanced Binary Tree*
    A binary tree is balanced if the height of the tree is O(logn) and will have the following prperties:

    1. the difference between the height of the left and the right subtrees is at most 1.

5. **Perfect Binary Tree**

    Def: A binary tree when all the internal nodes have two children and all leaf nodes are at the same level.

### **6.2 How to identify**

tree data structure in which each node has at most two children

### **6.3 Common tricks in Binary search**

1. Notice on the order. pre-order, in-order, and post-order use dfs while level order use bfs
2. Almost all questions can do on iterative and recursive methods
3. Knowing when to return value from recursion
    * When just output the node by traversing, no need to return
    * When calculation height then we need to return
4. Tricks:

    ```Python
    # for iterative approach on question like max depth, Symmetric Tree
    #1. put node in stack or Iterative traversal starting point
    stack = [(root, 1)  # #104. Maximum Depth of Binary Tree
    stack = [(root.left, root.right)]  # 101. Symmetric Tree
    stack = [(root, numSum-node.val)]  # #112. Path Sum
    stack = [root]  #144. Binary Tree Preorder Traversal
    ```

5. Question summary
    * Basics
        * #144. Binary Tree Preorder Traversal
        * #94. Binary Tree Inorder Traversal
        * #145. Binary Tree Postorder Traversal: Note that the iterative method between #94 and #145 are very similar
        * #102. Binary Tree Level Order Traversal
    * Tree depth related
        * #104. Maximum Depth of Binary Tree
        * #112. Path Sum
    * Symmetric, Rotated Tree
        * #101. Symmetric Tree

### **6.4 Common mistake points**

---

## **Heap**

### **7.1 Definition**

A special tree-based data structure in whicn tree is a complete binary tree. Heap is usually the way we build priority queue. It is logically a tree but implemented in an unsorted array with special rule to follow physicially.

Heap has certain properties:

1. Min/Max Heap: the smallest/biggest element at the root. A complete binary tree which the value in the internal mode is smaller/bigger or equal to the children's node.
2. What is the physicall rule of heap:

    2.1 Zero index based

    ``` Python
    # For 0-index based
    left_child_node_index = parent_node_index * 2 + 1
    right_child_node_index = parent_node_index * 2 + 2
    parent_node_index = (child_node_index - 1)//2
    ```

    2.2 One index based: **the index position is not used**

    ``` Python
    # For 1-index based
    left_child_node_index = parent_node_index * 2
    right_child_node_index = parent_node_index * 2 + 1
    parent_node_index = child_node_index // 2
    ```

3. Operations on heap (min heap for example since most are min heap)

    3.1 Time complexity:

    * insert/offer O(logn): Since the height is logn in binary tree so the max steps that the insert node need to move is O(logn)
    * update O(log): it is possible that we need to traverse the node
    * get O(1): Use the rule in the above
    * pop/poll O(logn): Same reason as insert node to heap. Same as pop the min value
    * heapify O(n): Need to walk through all elements

### **7.2 How to identify**

By knowing that it is a complete binary tree with heap order.

### **7.3 Common tricks in Heap**

### **7.4 Common mistake points**

1. `heapq.heappushpop()` vs `heapq.heapreplace() (assume min heap)`
    * `heapq.heappushpop()` push the element first and pop the smallest, so the smallest is guaranteed but the heap will not maintain fix size.
    * `heapq.heapreplace()` pop the element first the push the element, you may not save the smallest element but the heap is fix size.
2. `heapq.heapify()`
    * It tranform a list into heap but will NOT return the heap

    ```Python
    # wrong
    nums = [15,2]
    nums = heapq.heapify(nums)

    # correct
    nums = [15,2]
    heapq.heapify(nums)
    ```

## **DFS / BFS**

### **8.1 Definition**

### **8.2 How to identify**

### **8.3 Common tricks in DFS / BFS**

### **8.4 Common mistake points**

## **Graph**

### **9.1 Definition**

### **9.2 How to identify**

### **9.3 Common tricks in Graph**

### **9.4 Common mistake points**

## **Hash Table**

### **10.1 Definition**

### **10.2 How to identify**

### **10.3 Common tricks in Hash Table**

1. Type 1 - remove, lookup operations that need hash table or set
    1. Use list to save the result then use "".join instead
    2. Use hash table or set for look up operations since it spend O(1) time

### **10.4 Common mistake points**

## **Dynamic Programming**

### **11.1 Definition**

### **11.2 How to identify**

### **11.3 Common tricks in Dynamic Programming**

### **11.4 Common mistake points**
