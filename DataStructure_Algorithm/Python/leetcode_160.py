# Intersection of Two Linked Lists
# sol1: brut fource O(n^2), O(n)
# sol2: O(n+m), O(n)
# sol3: O(2(n+m)), O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getListLength(self, head):
        length = 0
        cur = head
        while cur is not None:
            cur = cur.next
            length += 1
        return length
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        size_a = self.getListLength(headA)
        size_b = self.getListLength(headB)
        diff = abs(size_a - size_b)
        a, b = headA, headB
        
        if size_a >= size_b:
            for _ in range(diff):
                a = a.next
        else:
            for _ in range(diff):
                b = b.next
        
        while a != b:
            a = a.next
            b = b.next
        return a