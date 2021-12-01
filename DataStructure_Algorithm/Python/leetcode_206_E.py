# Reverse a LinkedList

# create a ListNode first
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# iteration
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
  null  node1 -> node2 | -> node3
         prev   cur    nextnode  
        node1 <- node2 | -> node3
        1 <- 2 -> 3
           prev  <- cur  nextNode
        """
        # base case: when no need to reverse
        if not head or not head.next:
            return head
        cur = head
        prev = None
        while not head:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        return prev
            
            
# recursion
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        node1 -> | node2 -> node3 -> None
        node1 ->   node2 -> node3
        node1 <-  node2 <- node3
        
        """
        # base case: smallest problem
        if not head or not head.next:
            return head
        # recusive rule: repeatly solvable unit
        newHead = self.reverseList(head.next)  # node3
        head.next.next = head
        head.next = None
        return newHead # always newHead
        
