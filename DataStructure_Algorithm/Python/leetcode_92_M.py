# 92. Reverse Linked List II

# Definition for singly-linked list.
# iterate till one step behind lef
# reverse till
# post processing, the first part to tail of the reversed, the second part to head of the reversed

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next  # the point one step behind the reverse part

        cur = prev.next
        rev = None
        for _ in range(right - left + 1):
            nextNode = cur.next  # pioneer
            cur.next = rev  # cur index reverse
            rev = cur  # the later follows
            cur = nextNode  # pass to successor

        prev.next.next = nextNode  # 1 -> 2 <- 3 <- 4 5
        prev.next = rev

        return dummy.next
