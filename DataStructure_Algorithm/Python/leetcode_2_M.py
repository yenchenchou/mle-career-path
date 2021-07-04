# 2. Add Two Numbers

# Soulution1: Iternation 1
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # [2,4,3], [5,6,4] -> 342 + 465 -> 807 -> [7,0,8]
        # [2,1] + [1,7,9]-> 12 + 971 ->  983 -> [3,8,9]
        # 7, 0, 4+3+1
        # 3, 8, 9
        cur = head = ListNode(0)
        num = 0
        while l1 or l2 or num:
            if l1:
                num += l1.val  # use numto record all value together to solve when list with different length
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            # 3,4. 4,6
            cur.next = ListNode(num % 10)
            cur = cur.next
            num //= 10
            # [1], [9] -> 10 -> [0,1]
        return head.next

