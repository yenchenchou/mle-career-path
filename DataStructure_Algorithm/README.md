# **Coding Path**

## **1. Sorting**

1. Quick Sort
2. Merge Sort
3. Selection Sort
4. bubble osrt

### **1.2 How to identify**

### **1.3 Common tricks in Binary search**

1. Sort questions are commonly connect with heap or even replaced by heap
2. Question summary
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
    * Format:

    ```Python
    Initial Condition: left = 0, right = length-1
    Termination: left > right
    Searching Left: right = mid-1
    Searching Right: left = mid+1
    # final place for the pointers
    # [1, 2, 3, 4]
    #        l
    #     r
    ```

2. Type 2:
    * An advanced way to implement Binary Search.
    * Search Condition needs to access element's immediate right neighbor
    * Use element's right neighbor to determine if condition is met and decide whether to go left or right
    * **Gurantees Search Space is at least 2 in size at each step (because left ,< right)**
    * Post-processing required. Loop/Recursion ends when you **have 1 element left**, such as `while left < right`. Need to assess if the remaining element meets the condition.
    * There is a chance that we need to examine right neignbor index
    * Format:

    ```Python
    Initial Condition: left = 0, right = length-1
    Termination: left == right
    Searching Left: right = mid
    Searching Right: left = mid+1
    # final place for the pointers
    # [1, 2, 3, 4]
    #     l
    #     r
    ```

3. Type 3:
    * An alternative way to implement Binary Search
    * Search Condition needs to access element's immediate left and right neighbors
    * Use element's neighbors to determine if condition is met and decide whether to go left or right
    * Gurantees Search Space is at least 3 in size at each step
    * Post-processing required. Loop/Recursion ends when you have 2 elements left. Need to assess if the remaining elements meet the condition.
    * Format:

    ```Python
    Initial Condition: left = 0, right = length-1
    Termination: left <> right
    Searching Left: right = mid
    Searching Right: left = mid
    # final place for the pointers
    # [1, 2, 3, 4]
    #     l
    #        r
    ```

4. Other tricks or self summary
    * Check if `left <= right`, `left < right`, or `left < right - 1`
    * **Compare with the target value or left most, right most, left neighbor, right neighbor**
    * Whether skipping the mid is correct way
    * Becareful of index out of bound when point 1 is specified

5. Question summary
    * square root/pow/product related problems, guess number (usually `left <= right`):
        * #69 Sqrt
        * #367 Valid Perfect Square
        * #50 Pow
        * #374. Guess Number Higher or Lower
    * Rotated:
        * #33. Search in Rotated Sorted Array
        * #153. Find Minimum in Rotated Sorted Array (distinct: use left < right)
        * #154. Find Minimum in Rotated Sorted Array II
    * Comparing left/right index in comparision, neighbor, return left/right index instead, First/last occurence (range):
        * #35. Search Insert Position
        * #162. Find Peak Element
        * #278. First Bad Version
        * #34. Find First and Last Position of Element in Sorted Array (two ways of thinking first/last)
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

1. design linked list:
    * delete node in linkedlist:
        * unique/duplicates node to delete:
            * two pointer: one `cur` and one `prev` + let `prev.next` pointer point to `cur.next`
            * value replacement:

                ```Python
                node.val = node.next.val
                node.next = node.next.next
                ```

    * insert node:
        * with cycle:
            * same as inserting on arch cycle but consider:

                ```Python
                if prevNode.val <= insertVal <= curNode.val:
                # min / max value is serted
                elif preNode.val > curNode.val and (insertVal < curNode.val or insertVal > preNode.val)
                
                # remember to stop when all nodes are smaller / bigger than the inserted one
                ```

2. cycle/two pointers:
    * fast and slow pointer
    * Always examine if the node is null before you call the next field. When `fast = fast.next.next`, we need to examine `fast`, `fast.next` before to prevent null error.
3. reverse
    *
4. combine with common algorithms
    * mergesort a linked list
5. Floyd's Tortoise and Hare
6. Question summary
    * design linked list:
        * #707 Design a Singly/Double LinkedList
        * #21: Merge Two Sorted
        * #203 Remove Linked List Elements
        * #19 Remove Nth Node From End of List
        * #237. Delete Node in a Linked List
        * #328 Odd Even Linked
        * #708. Insert into a Sorted Circular Linked List (insertation)
    * cycle / fast slow pointer / two pointers
        * #141 Cycle in LinkedList
        * #142 LinkedList Cycle II (**)
        * #160 Intersection of Two Linked
        * #19. Remove Nth Node From End of List
    * reverse
        * #206 Reverse a LinkedList
        * #344 Reverse a string and swap the string in place(344 M): sentinel node concept, rescurion
        * #234 Palindrome Linked List
    * combine with common algorithms
        * stack:
            * #430. Flatten a Multilevel Doubly Linked List

### **3.4 Common mistake points**

1. When youde-reference a ListNode, make sure it is not a NUll pointer
2. Never lost conrol of the head pointer
3. Usually, we have no idea where is the head, we need a dummy node to handle that

### **Recursion**

---

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

## **Queue and Stack**

---

### **5.1 Definition**

Queue is a linear structure that follow first-in-first-out policy. Queue some how represent some fairness, which means the one waiting the longest will be the first to be served. It is also a piece in asynchronous computation. On the other hand, Stack follows first-in-last-out.

### **5.2 How to identify**

1. Stack: When you need to continuously look back at the last element of left/right.
2. Queue: when you want to get things out in the order that you put them in.

### **5.3 Common tricks in Queue and Stack**

1. Calculator problem: Notice that the `cur`(the current calculated digit) and the `sign`(the pos/neg flag) will be updated when face none digit.

### **5.4 Common mistake points**

1. Question summary
    * Tree point by level
    * Sliding window
    * The largest rectangle in histogram
    * reverse polish notation
    * repeat deduplication of a String
    * Classic Queue:
        * #346. Moving Average from Data Stream
    * Classic Stack:
        * #125. Valid Palindrome
        * #1047. Remove All Adjacent Duplicates In String
        * #155. Min Stack
        * #716. Max Stack
    * Handle parentheses, calculator
        * #224. Basic Calculator
        * #227. Basic Calculator II
        * #394. Decode String
    * Greedy, duplicates:
        * #316. Remove Duplicate Letters
    * mix with heap, linkedlist:
        * #716. Max Stack

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

Tree data structure in which each node has at most two children

### **6.3 Common tricks in Binary search**

1. Notice on the order. pre-order, in-order, and post-order use dfs while level order use bfs
2. Almost all questions can do on iterative and recursive methods
3. Knowing when to return value from recursion, what to expect when you return the value from the recursive function
    * When just output the node by traversing, no need to return
    * When calculation height then we need to return
4. Level Order Traversal Tricks:
    * When using iterative approach, how do we keep track of the level and value

    ```Python
    # for iterative approach on question like max depth, SymmetrFic Tree
    #1. put node in stack or Iterative traversal starting point
    stack = [(root, 1)  # #104. Maximum Depth of Binary Tree
    stack = [(root.left, root.right)]  # 101. Symmetric Tree
    stack = [(root, numSum-node.val)]  # #112. Path Sum
    stack = [root]  #144. Binary Tree Preorder Traversal
    ```

    * Thick how to reduce the space while need to track the level -> depth problem, hybrid problems
5. Tips to decide when write to the process code

    ```Python
    def dfs(root):
        # Write the steps here if you want to do something top to down
        dfs(root.left)
        dfs(root.right)
        # Write the steps here if you wanr too something down to top -> path, counting
    ```

6. When to something for the recursion tree
    * When expecting something to return at root.left / root.right

    ```Python
    def dfs(root):
        if not root: return <val>  # the data type align with the lower return 
        left = dfs(root.left)  # You are hoping to return from root.left
        right = dfs(root.right)  # You are hoping to return from root.right
        return left/right  # The return here decide what to return to left/right
    ```

    * Example1: When just returning True/False

    ```Python
    # Instead of this
    def dfs(root):
        if not root: return <val> 
        left = dfs(root.left)
        right = dfs(root.right)
        return left or/and right
    ```

    ```Python
    # Do this
    def dfs(root):
        if not root: return <val> 
        return dfs(root.left) or/and dfs(root.right)
    ```

7. When comparing value with child/parent/neighbors
    * Think of creating a new helper function and use `max/min` to compare
    * the helper function may cointains more than the node, such as the value `helper(root, root.val)`

8. Question summary
    * Basics
        * #144. Binary Tree Preorder Traversal
        * #94. Binary Tree Inorder Traversal
        * #145. Binary Tree Postorder Traversal: Note that the iterative method between #94 and #145 are very similar
        * #102. Binary Tree Level Order Traversal
        * #572. Subtree of Another Tree
        * #236. Lowest Common Ancestor of a Binary Tree
        * #103. Binary Tree Zigzag Level Order Traversal
    * Tree depth related
        * #104. Maximum Depth of Binary Tree
        * #112. Path Sum
        * #250. Count Univalue Subtrees
    * Comparing value with child/parent/neighbors
        * #543. Diameter of Binary Tree
        * #98. Validate Binary Search Tree
        * #1448. Count Good Nodes in Binary Tree
    * Symmetric, Rotated Tree
        * #101. Symmetric Tree
        * #226. Invert Binary Tree
    * Tree construction: observe the relationship btw two data structure
        * #105. Construct Binary Tree from Preorder and Inorder Traversal
        * #106. Construct Binary Tree from Inorder and Postorder Traversal
    * Hybrid: (diff ways to keep track of layer)
        * Tree+LinkedList+Queue: #116. Populating Next Right Pointers in Each Node
        * #117. Populating Next Right Pointers in Each Node II

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

1. Max heap: most heap in programming languafe is min heap. So we use Counter with negative to do the count.
2. Question summary
    * Basic:
        * Use arrya design heap
    * Top K questions (You may sort to solve these problems):
        * #703. Kth Largest Element in a Stream
        * #215. Kth Largest Element in an Array (alike 703)
        * #347. Top K Frequent Elements
        * #692. Top K Frequent Words (advanced of #347)
        * #451. Sort Characters By Frequency (advanced of #347)

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

1. DFS: You start at the root node or starting position and explore as far as possible. Usually invlove with the followings, see [Python example](https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python):
    * recusion (not required) / Iteration + stack
    * mark current node as visited
    * go through all adjacent node if not visited

    ```bash
    # Iterative
    procedure DFS_iterative(G, v) is
        let S be a stack
        S.push(iterator of G.adjacentEdges(v))
        while S is not empty do
            if S.peek().hasNext() then
                w = S.peek().next()
                if w is not labeled as discovered then
                    label w as discovered
                    S.push(iterator of G.adjacentEdges(w))
            else
                S.pop()

    # Recursive
    procedure DFS(G, v) is
        label v as discovered
        for all directed edges from v to w that are in G.adjacentEdges(v) do
            if vertex w is not labeled as discovered then
                recursively call DFS(G, w)
    ```

2. BFS: You start at the root node or starting position and explore the neighbors, see [Python example](https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python)
    * Iteration
    * use quueue
    * mark current node as visited

   ```bash
    # Iterative appraoch
    procedure bfs(G, root) is
        let S be queue
        label root as discovered
        Q.enqueue(root)
        while Q is not empty:
            v := Q.dequeue()
            if v is the goal then
                return v
            for all edges from v to w in G.adjacentEdges(v) do
                if w is not discovered
                    label w as discovered
                    Q.enqueue(w)
    ```

### **8.2 Properies and Applications**

1 DFS:

* Produce minumum spanning tree
* Detect cycle
* Path finding
* Topological Sorting
* [Others](https://www.geeksforgeeks.org/applications-of-depth-first-search/)

2 BFS:

### **8.3 Common tricks in DFS / BFS**

1. DFS
    * Use stacks
    * Use hashmap/set
    * Use recursion
2. BFS
    * Use queue
    * use hashmap/set
3. Backtracking: happens in recursion a lot
    * A general algorithm that finds all solutions to some problems, which incrementally build candidates and abandon candidates when it does not lead to a valid solution. The backtrack meaning is due to when you find the certain point that does not lead to a solution, and you "backtrack" to its parent for other opportunities.
    * A better than bruce force if one remember to handle seen situations.
    * In tree problems, it is also known as pruning.
    * Example: N-Queen
    * Template

    ```Python
    def backtrack(candidate):
        if find_solution(candidate):
            output(candidate)
            return
        
        # iterate all possible candidates.
        for next_candidate in list_of_candidates:
            if is_valid(next_candidate):
                # try this partial candidate solution
                place(next_candidate)
                # given the candidate, explore further.
                backtrack(next_candidate)
                # backtrack
                remove(next_candidate)
    ```

### **8.4 Common mistake points**

1. It is not neccesary to create a set/hashmap to store seen flag everytime, instead just replace the original value

2. Question Summary:
    * Basics (simpla dfs/bfs, or island related problems):
        * #200. Number of Islands
        * #695. Max Area of Island
        * #1727. Largest Submatrix With Rearrangements
        * #463. Island Perimeter
        * #547. Number of Provinces
    * Combinations:
        * #17. Letter Combinations of a Phone Number
    * Backtrack:
        * #51. N-Queens
        * #207. Course Schedule

## **Graph**

### **9.1 Definition**

An abstract notation that used to represent the connection between objects. A grpah consist of vertices `V` and edges `E`. Often grpah is noted as `G(V, E)`. Every edge in E connects two vertices V. A graph could be directed and undirected grpah.

```Python
# Undirected
G = (V, E)
V = (a, b, c)
E = {(a, b), (b, c), (a, c)}

# Directed
G = (V, E)
V = (a, b, c)
E = {(a, b), (b, c), (c, b), (a, c)}
```

### **9.2 How to identify**

When you see objects has vertices(nodes) and pointers(edges)

### **9.3 Common tricks in Graph**

1. Use adjacency matrix to record whether there are edges between vertices. But waste space and hard to add new vertex
2. Use hashtable is better on flexibility, space, and speed
3. Other common algorithms
    * Topological sort/ordering
        * Def: Topological ordering is a directed graph where the directed edge AB, the A will always comes before B
        * Application:
            * Finding cycle: use the def to find
        * Implementation:
            * Kahn's Algorithm
                * Def: repeat to process of removing node without dependencies (and their outgoing edges)
                * How:
                    1. Calculate the dependencies(incoming edge) and start with the node with 0 dependencies,
                    2. Then add to queue
                    3. Process then remove from, update the dependencies array and add the new nodes with no dependencies
                    4. use an index to count the nodes that put into sorting process
                    5. check if # of nodes == index, if not then there is at least a cycle since some of the nodes are not processed
    * Uinion find

### **9.4 Common mistake points**

## **Hash Table**

### **10.1 Definition**

### **10.2 How to identify**

### **10.3 Common tricks in Hash Table**

1. remove, lookup operations that need hash table or set
    1. Use list to save the result then use "".join instead
    2. Use hash table or set for look up operations since it spend O(1) time

### **10.4 Common mistake points**

1. Need to avoid duplication so may use a set/hashtable to address the problem

## **Dynamic Programming**

### **11.1 Definition**

### **11.2 How to identify**

### **11.3 Common tricks in Dynamic Programming**

### **11.4 Common mistake points**
