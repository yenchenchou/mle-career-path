# Remove Nth Node From End of List
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = next


# Solution1: two pass
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        while head:
            head = head.next
            length += 1
        new_dummy = dummy
        for _ in range(length - n):
            new_dummy = new_dummy.next
        new_dummy.next = new_dummy.next.next
        return dummy.next


# Solution2: two pointer with one pass
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = ListNode(0)
        node.next = head

        first = node
        second = node
        for _ in range(n + 1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return node.next
