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
        # if not head or not head.next: return head
        # slow = fast = head
        # while fast and fast.next:  #  fast.next is needed otherwise null poiter execption
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow

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

# 4. insert a node in a sorted list

# 5. How to merge two sorted list 

# 6. Convert N1 -> N2 -> N3 -> N4 -> N5  -> N6 -> … -> Nn -> null to  (N1 -> Nn) -> (N2 -> Nn-1) -> ... 


# 7. Partition List Given a linked list and a target value x, partition it such that all nodes less than x are linked before the node larger than or equal to target value x. (Keep the original relative order of nodes in each of the two partitions).
