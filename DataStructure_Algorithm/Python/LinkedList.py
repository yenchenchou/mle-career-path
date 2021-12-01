"""
Basics of LinkedList:
1. the next pointer is to record the physical address of the other node

Important points:
1. Never lost control of the head node
2. When you want to de-reference a ListNode, becareful of null pointer error. null pointer: node.val = NULL. The action of node.val is de-reference
3. When you need head dummy node: When we want to append a new elements to an initially empty LinkedList, we don't not have an initial head node. In this case we can create a dummy node.
4. When you need tail dummy node: When we need to append new element to an existing LinkedList
"""
# 1. reverse LinkedList

# 2. Middle node

# 3. Check if there is a cycle

# 4. insert a node in a sorted list
#   3 -> 7, insert 0
# corner cases
## insert can be tail, so need a dummy head, treat just like insert in the middle and easier to handle
## insert can be tail, null pointer error

# 5. Convert N1 -> N2 -> N3 -> N4 -> N5  -> N6 -> … -> Nn -> null to  (N1 -> Nn) -> (N2 -> Nn-1) -> ... 
# get the middle node and the middle node treat as a head of left half linkedlist. the next node of head of right half
# reverse the right half linkedlist
# merge two half of the linkedlist
# note: maintain two tail pointers, one for merge one for the null pointer, because the last element may originally connect to other nodes

# 6. Partition List Given a linked list and a target value x, partition it such that all nodes less than x are linked before the node larger than or equal to target value x. (Keep the original relative order of nodes in each of the two partitions).
