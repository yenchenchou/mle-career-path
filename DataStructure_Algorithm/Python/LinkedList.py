"""
Basics of LinkedList:
1. the next pointer is to record the physical address of the other node

Important points:
1. Never lost control of the head node
2. When you want to de-reference a ListNode, becareful of null pointer error. null pointer: node.val = NULL. The action of node.val is de-reference
3. When you need head dummy node: When we want to append a new elements to an initially empty LinkedList, we don't not have an initial head node. In this case we can create a dummy node.
4. When you need tail dummy node: When we need to append new element to an existing LinkedList
"""
# 1. reverse a linked list
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(head):
    ls = []
    temp = head
    while temp:
        ls.append(temp.val)
        temp = temp.next
    return ls

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Option1: iterative (from left to right)
        1. corner case: when empty or only one node
        2. need next pointer, and prev pointer 
        3. Once create the next pointer, we are not afraid changing the cur pointer because next_node knows the remainings 
        4. cur.next = prev
        3. cur and prev go a step forward
        Time: O(n)
        Space: O(n)

None    1   ->   2   ->   None
        
         None <- prev  <- cur      next -> 

        None  <-   1   <-   2 

        Option2: recursive (right to left)
        1.    --------------
        1 -> | 2 -> None   | 
              --------------
        None <- 1 <- | treat as one thing|
        Time: O(n)
        Space: O(1) -> only the pointer is changing, not the actual value

        """
        # Option1
        if not head or not head.next: return head
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head  # prev first, before the head moves to next node
            head = next_node
        return prev

        # Option2
        if not head or not head.next: return head
        # newhead because the recursive function runs to the end of the linkedlist
        # recursion stop at the last node, when this release from the stack, we are at the second last node, just like the above illustration
        newHead = self.reverseList(head.next)
        # let the last node point to second last (reverse happens at here)
        head.next.next = head
        # now one poiter to left + one to left -> we need to cancel the one points to the right
        head.next = None
        return newHead  # the newHead never changed since the first time we reach the base case

def test1():

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    sol = Solution()

    assert printList(sol.reverseList(node1)) == [3,2,1]


def test2():

    node1 = ListNode(1)

    sol = Solution()

    assert printList(sol.reverseList(node1)) == [1]

test1()
test2()
 
# 2. 876. Middle of the Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        # If there are two middle nodes, return the second middle node.
        1. corner cases: if not head or one node
        2. use two pointers, one two steps a time and the other one is one step a time
        1 -> 2 -> 3 -> 4 -> none
                  s
                            f

        # follow up, what about first middle node this time?
        1 -> 2 -> 3 -> 4 -> none
             s
                       f
        1 -> 2 -> 3 -> 4 -> 5 -> none
                  s
                                  f
        -> option1: make sure fast.next.next exist
        -> option2: fast pointer with one step ahead staring point
        """
        # Option1
        if not head or not head.next: return head
        slow = fast = head
        while fast and fast.next:  #  fast.next is needed otherwise null poiter execption
            slow = slow.next
            fast = fast.next.next
        return slow

        # Follow up - option1
        if not head or not head.next: return head
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        # Follow up - option2
        if not head or not head.next: return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# 3. Check if there is a cycle in the LinkedList
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        1. corner case: if not and one node
        2. when it is possible: when slow and fast pointer overlaps (Floyd's Cycle Finding Algorithm)
            -> how to place fast / slow pointer

        # no matter where we start slow/fast, they will eventually come together, 
        # but the point is how about one element, it will not fit if they start at same position
            -> need different starting point to get into loop
        1 -> 2 -> 3 -> 4 
                  <-----

        1 -> None
        s    f
        """
        if not head: return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

# 4. insert a node in a sorted list (use 707. Design Linked List as alternative example)
def insert_node(head, node):
    """
    insert position:
    -> midlle
    dummy -> 1 -> 3 -> none
            cur
    insert 0 
    -> the insert node points to the node with bigger value then the smaller node change to the new inserted node

    -> head
    point to head directly and make it as new head

    -> tail
    iterate till the end
    
    1. if the current node val is smaller than inserted node val than current node point to next and cur.next exist
    2. the inserted mode point to what the current.next is pointing to
    3. current node point to new node

    Time: O(n)
    Space: O(1)
    """
    # corner case
    if not head: return node
    if not node: return -1
    dummy = ListNode(float("-inf"))
    dummy.next = head
    cur = dummy  # never lost head
    while cur.next and cur.next.val < node.val:
        cur = cur.next
    node.next = cur.next
    cur.next = node
    return dummy.next


def test1():
    newnode = ListNode(0)

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    assert printList(insert_node(node1, newnode)) == [0,1,2,3]


def test2():
    newnode = ListNode(4)

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    assert printList(insert_node(node1, newnode)) == [1,2,3,4]


def test3():
    newnode = ListNode(1)

    node1 = ListNode(0)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    assert printList(insert_node(node1, newnode)) == [0,1,2,3]


test1()
test2()
test3()

# 5. How to merge two sorted list 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        we have no idea where is the head at first -> dummy head as start, return dummy.next
        1. if list1 is none / used up -> return list2
        2. same for list2
        3. both none, return None

        1->4->5->none
                 p1
        3->5->100->none
          p2
        dummy -> 1 -> 3 -> 4 -> 5 -> p2
                              dummy
        """
        # corner case
        if not list1 and not list2: return None
        newhead = ListNode(0)
        dummy = newhead
        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        return newhead.next
            

# 6. Convert N1 -> N2 -> N3 -> N4 -> N5  -> N6 -> … -> Nn -> null to  (N1 -> Nn) -> (N2 -> Nn-1) -> ... 
## Alternative practice: 24. Swap Nodes in Pairs
class PairListSolution:
    def pair_list(self, head):
        """
        1 -> 2 -> 3 -> 4 - > 5
        (1 -> 5) -> (2 -> 4) -> 3
        1. use fast slow pointer to find middle point
        2. reverse the second half
        3. pair the nodes
        Time: middle O(n) + reverse O(n) + merge O(n) -> O(n)
        Space: middle O(1) + reverse O(1) + merge O(1) -> O(1s)
        """
        # corner case
        if not head or not head.next: return head
        newhead = ListNode(0)
        dummy = newhead
        mid = self.find_middle(head)  # if even number of nodes, choose the first middle point
        reversed_head = self.reverse_list(mid.next)
        mid.next = None  # cut the next pointer from the middle point

        while head and reversed_head:
            dummy.next = head
            head = head.next
            dummy = dummy.next
            dummy.next = reversed_head
            reversed_head = reversed_head.next
            dummy = dummy.next  
        # printList(dummy.next) 
        if head:
            dummy.next = head
        if reversed_head:
            dummy.next = reversed_head
        return newhead.next

    def find_middle(self, head):
        # 1-2-3
        if not head or not head.next: return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head):
        if not head or not head.next: return head
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head  # prev first, before the head moves to next node
            head = next_node
        return prev
    

def test1():
    sol = PairListSolution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    assert printList(sol.pair_list(node1)) == [1,5,2,4,3]


def test2():
    sol = PairListSolution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    assert printList(sol.pair_list(node1)) == [1,4,2,3]


def test3():
    sol = PairListSolution()

    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    assert printList(sol.pair_list(node1)) == [1,4,1,3]


test1()
test2()
test3()


# 7. Partition List Given a linked list and a target value x, partition it such that all nodes less than x are linked before the node larger than or equal to target value x. (Keep the original relative order of nodes in each of the two partitions).
## 86. Partition List
def partition_list(head, x):
    """
    10 -> 2 -> 15 -> 7 -> 4 ->  none, traget=10
                         head
    2 -> 7 -> 4 -> 10 -> 15
    left_dummy -> 2 -> 7 -> 4
                            l.next -> r.next
    right_dummy -> 10 -> 15 -> (7) to None
                          r
    1. two new linkedlist, with dummy head. For value < target append to the first list, value => target append to second one
    2. Need dummy head for first node, need tail pointer since we need to keep appending values
    3. Once the process is completed, let the tail.next point to head of the second list. 
    ## NOTE: remember to to let the tail.next = None to avoid cycle

    Time: O(n)
    Space: O(1)
    """
    # corner case
    if not head or not head.next: return head
    left_half, right_half = ListNode(0), ListNode(0)
    left_dummy = left_half
    right_dummy = right_half
    while head:
        if head.val < x:
            left_dummy.next = head
            left_dummy = left_dummy.next
        else:
            right_dummy.next = head
            right_dummy = right_dummy.next
        head = head.next
    right_dummy.next = None
    left_dummy.next = right_half.next
    return left_half.next


def test1():

    node1 = ListNode(10)
    node2 = ListNode(2)
    node3 = ListNode(15)
    node4 = ListNode(7)
    node5 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    assert printList(partition_list(node1, 10)) == [2,7,4,10,15]


def test2():

    node1 = ListNode(1)
    node2 = ListNode(10)
    node3 = ListNode(10)
    node4 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    assert printList(partition_list(node1, 3)) == [1,1,10,10]


def test3():
    sol = PairListSolution()

    node1 = ListNode(1)
    assert printList(partition_list(node1,2)) == [1]


def test4():

    node1 = ListNode(1)
    node2 = ListNode(-1)
    node1.next = node2

    assert printList(partition_list(node1, 2)) == [1, -1]


test1()
test2()
test3()
test4()