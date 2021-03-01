# Palindrome Linked List
# concept: reversed linked list, slow and fast pointer(Optional)


# Sol1: Best 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reveseList(self, head):
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev
            
    def rightPartList(self, head):
        left, right = head, head
        while right.next and right.next.next:
            right = right.next.next
            left = left.next
        return left
    
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        first_half_end = self.rightPartList(head)
        right = self.reveseList(first_half_end.next)
        left = head
        while left and right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True 
# Time: O(n+n) -> O(n), Space: O(1) -> we do not save the list each intermediate output is just the pointer
# Tese Cases: [None], [1], [1, 2], [1, 1], [1, 2, 1], [1, 1, 1], [1, 1, 3], [1,2,3,2,1]


# Solution2: My try          
class Solution:
    def reveseList(self, head):
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev
            
    
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
            
        left, right = head, head
        for _ in range(length//2):
            right = right.next
        right = self.reveseList(right)
            
        while left and right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True #[None], [1], [1, 2], [1, 1], [1, 2, 1], [1, 1, 1], [1, 1, 3], [1,2,3,2,1]


# Solution3: Recursion

 