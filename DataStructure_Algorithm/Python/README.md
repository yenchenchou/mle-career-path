# **Coding Path**

## **1. Sorting**

## **2. Binary Search**

### **2.1 Definition**

Binary Search operates on a contiguous sequence with a specified left and right index. The left, right, mid index helps us to compare the target. If the  index shows the condition deos not align with the target then that half part is eliminated. We do this repeatly then get the final result.

When solving binary search, there are several things included most of the time:

1. target: the target value you are searching for. Can be something around target
2. index: the current location that you are searching
3. left, right: the indices from which we use to maintain our search space
4. mid: the index used to apply a condition to determine if we should saerch left or right

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

3. Type 3:

4. Other tricks

5. Other summary
    * square root related problems: #69, #367

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

A data structure in which each node has at most two children, which are referred to as the left child and the right child.