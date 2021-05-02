# 708. Insert into a Sorted Circular Linked List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: "Node", insertVal: int) -> "Node":
        # just like normal insert node
        # 1347 insert 2 5
        # 1-2-3-4-5, 0 6
        # 1 insert 0
        if not head:
            head = ListNode(insertVal)
            head.next = head
            return head
        node = ListNode(insertVal, head)
        minp = head
        maxp = head.next
        while True:
            if minp.val <= insertVal <= maxp.val:
                break
            elif minp.val > maxp.val and (insertVal < maxp.val or insertVal > minp.val):
                break
            minp = minp.next
            maxp = maxp.next
            # Means we made a complete cycle without breaking, meaning
            # all nodes are dupe vals (prev<=val<=cur doesn't hit because
            # val could be larger or smaller than the dupe).
            if minp == head:
                break
        node.next = maxp
        minp.next = node
        return head
