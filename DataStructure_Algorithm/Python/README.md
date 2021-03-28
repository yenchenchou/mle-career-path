# **Coding Path**

# **Algorithms**

## **1. Sorting**

## **2. Binary Search**

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
    1. Search Condition can be determined without comparing to the element's neighbors (or use specific elements around it)
    2. No post-processing required because at each step, you are checking to see if the element has been found. If you reach the end, then you know the element is not found
    3. Usually will invloved `while left <= right`, `left = mid + 1`, `right = mid - 1`, terminate at `left > right`

2. Type 2:
    1. An advanced way to implement Binary Search.
    2. Search Condition needs to access element's immediate right neighbor
    3. Use element's right neighbor to determine if condition is met and decide whether to go left or right
    4. **Gurantees Search Space is at least 2 in size at each step (because left ,< right)**
    5. Post-processing required. Loop/Recursion ends when you **have 1 element left**, such as `while left < right`. Need to assess if the remaining element meets the condition.
    6. There is a chance that we need to examine right neignbor index

3. Type 3:
    1. An alternative way to implement Binary Search
    2. Search Condition needs to access element's immediate left and right neighbors
    3. Use element's neighbors to determine if condition is met and decide whether to go left or right
    4. Gurantees Search Space is at least 3 in size at each step
    5. Post-processing required. Loop/Recursion ends when you have 2 elements left. Need to assess if the remaining elements meet the condition.

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
    * COmparing left/right index in comparision, neighbor, return left/right index instead:
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

### **2.4 Common mistake points**

## **3. LinkedList**

### **3.1 Definition**

1. Design a Singly LinkedList(707): sentinel node concept
2. Design a Double LinkedList(707): sentinel node concept
3. Merge Two Sorted Lists(21): sentinel node concept
4. Remove Linked List Elements(203 E): sentinel node concept
5. Cycle in LinkedList(141): sentinel node concept, fast slow two pointers
6. LinkedList Cycle 2(142): fast slow two pointers
7. Intersection of Two Linked Lists(160): fast slow two pointers
8. Remove Nth Node From End of List(19 M): sentinel node concept
9. Reverse a LinkedList(206 E): sentinel node concept, rescurion
10. Reverse a string and swap the string in place(344 M): sentinel node concept, rescurion
11. Odd Even Linked List(328 M):
12. Palindrome Linked List(234): sentinel node concept, fast slow two pointers

|               Question              | Difficulty |                  Concept                  | # Practice |
|:-----------------------------------:|:----------:|:-----------------------------------------:|:----------:|
|   Remove Linked List Elements(203)  |    Easy    |                  sentinel                 |      2     |
|      Merge Two Sorted Lists(21)     |    Easy    |                  sentinel                 |      2     |
| Design a LinkedList(707 - Singular) |    Easy    |        sentinel, next.next pointer        |      3     |
|  Design a LinkedList(707 - Double)  |    Easy    | sentinel, next.next pointer, reverse loop |     2*     |
|       Cycle in LinkedList(141)      |    Easy    |        sentinel, fast slow pointer        |      3     |
|                                     |            |                                           |            |

### **3.2 How to identify**

### **3.3 ommon tricks in Binary search**

### **3.4 Common mistake points**

## **Queue and Stack**

### **4.1 Definition**

### **4.2 How to identify**

### **4.3 ommon tricks in Binary search**

### **4.4 Common mistake points**

## **Recursion**

### **5.1 Definition**

### **5.2 How to identify**

### **5.3 ommon tricks in Binary search**

### **5.4 Common mistake points**

## **Binary Tree**

### **6.1 Definition**

### **6.2 How to identify**

### **6.3 ommon tricks in Binary search**

### **6.4 Common mistake points**

## **Binary Serch Tree**

### **7.1 Definition**

A node based binary tree with the following properties:

1. The left subtree of a node should only contains node with keys smaller than the node's key
2. The right subtree of a node should only contains nide with keys greater than the node's key
3. The left and right subtree each must also be a binary search tree
4. Some rare cases the right index doen't need to be len(arr)-1

### **7.2 How to identify**

### **7.3 ommon tricks in Binary search**

### **8.4 Common mistake points**

A data structure in which each node has at most two children, which are referred to as the left child and the right child. 

If the tree is balanced, we call a tree balanced if for all nodes the difference between the heights of left and right subtrees is not greater than one