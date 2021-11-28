# 2046. Sort Linked List Already Sorted Using Absolute Values

"""
Goal: 

1. 0 -> 2 -> -5 (two pointers, prev and cur. Jump when negative)
2. -5 -> 0 -> 5 (cur becomes new temp head, then move head to the right place)
3. Let cur pointer go back to one step ahead of prev

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        prev, cur = head, head.next
        while cur:
            if cur.val < 0:
                prev.next = cur.next
                cur.next = head
                head = cur
                cur = prev.next
            else:
                cur = cur.next
                prev = prev.next
        return head    # O(n), O(1)
