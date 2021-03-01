# LinkedList Cycle 2
# Instead of checking whether there is a intersection, we want the return the node where the intersection start

# sol1: hashing, O(n)/O(n)
# sol2: Floyd's Tortoise and Hare, which mean after the two pointer meet each other, we assign one of the pointer back to
#       the start point, then we let pointer1 and pointer2 walk at same speed, the two pointers will meet at the start of 
#       cycle everytime


class Solution:
    def hasCycle(self, head);
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return fast
        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        intersection = self.hasCycle(head)
        if intersection is None:
            return None
        p = intersection
        q = head
        while p != q:
            p = p.next
            q = q.next
        return p


# Question: why this logic is not working
def hasCycle(self, head);
    if head is None:
        return None
    fast = head.next
    slow = head
    while fast != slow:
        fast = fast.next.next
        slow = slow.next
        if fast is None or fast is None:
            return None
    return fast