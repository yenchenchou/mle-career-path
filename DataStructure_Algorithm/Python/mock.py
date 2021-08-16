"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = []
Output: []

"""




# start_node [ListNode, val = XXXX]
# start_node -> None
# start_node -> 1
# start_node -> 2 -> 1
# start_node -> 3 -> 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        start_node = ListNode(val=-1)

        # start_node -> 5 -> 4 ->3 -> 2 ->1
        # start_node -> 1
        #    V  
        # [1,2,3,4,5]
        while head:
            next_head = head.next # head = 1 next_head = 2
            # head = 2
            # start_node 
            # temp ->  
            temp = start_node.next
            start_node.next = head
            start_node.next.next = temp
            head = next_head
        return start_node.next