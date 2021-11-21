from typing import Dict


class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next= next


class SingleLinkedList:
    def __init__(self) -> None:
        self.head = ListNode(0)
        self.size = 0

    def get_at_index(self, index) -> None:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index+1):    
            cur = cur.next
        return cur.val

    def add_at_head(self, val) -> None:
        self.add_at_index(0, val)

    def add_at_tail(self, val) -> None:
        self.add_at_index(self.size, val)

    def add_at_index(self, index, val) -> None:
        if index < 0 or self.size < index:
            return -1
        node = ListNode(val)
        cur = self.head
        for _ in range(index):
            cur = cur.next
        node.next = cur.next
        cur.next = node
        self.size += 1

    def delete_at_index(self, index) -> None:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.head
        cur.next = cur.next.next
        self.size -= 1

    def swap_at_index(self, first_index, second_index) -> None:
        pass

    
