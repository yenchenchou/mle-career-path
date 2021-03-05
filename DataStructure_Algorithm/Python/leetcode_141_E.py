# Determine if there is cycle in LinkedList
# Sol1: use hashmap 
# sol2: Floyd's Cycle Finding

class Solution:
    def hasCycle(self, head: Listnode) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False


# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         if head is None:
#             return
#         slow = head
#         fast = head.next
#         while slow != fast:
#             if fast is None or fast.next is None:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
#         return True

    # Space: O(1)
    # Time: O(n) -> 
        # No cycle: O(n)
        # With cycle: consider two pointers are in the cycle in a length of k <= n linked list,
        # since the speed of fast pointer is two times the slow pointer, it takes at most k
        # to meet the fast pointer, so O(n + k) = O(2n) = O(n)
        
