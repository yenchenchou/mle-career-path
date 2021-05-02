# 328 Odd Even Linked List

# solution1: iteration
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd, even = head, head.next
        evenHead = even  # all odd -> all even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head

    # [1, 2, 3],Time: O(n), Space: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # [1,2,3,4]
        #    o e
        #
        if not head:
            return head
        odd, even = head, head.next
        evendummy = even
        while evendummy and evendummy.next:
            odd.next = evendummy.next
            odd = odd.next
            evendummy.next = odd.next
            evendummy = evendummy.next
        odd.next = even
        return head