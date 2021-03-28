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
    #[1, 2, 3],Time: O(n), Space: O(1) 


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
    #[1, 2, 3],Time: O(n), Space: O(1) 