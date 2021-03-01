# Reverse a LinkedList
class ListNode:
    def __init__(self, val):
        self.val = val 
        self.next = None


# solution1.2: loop 
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev
        # None, [None, 1], [None, 1, 2], [None, 1, 2, 3]

# solution1.2: loop -> why this work?
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        cur = head
        while head.next is not None:
            p = head.next
            head.next = p.next
            p.next = cur
            cur = p
        return cur
        # None, [None, 1], [None, 1, 2], [None, 1, 2, 3]


# solution2: recursion
class Solution:
    pass