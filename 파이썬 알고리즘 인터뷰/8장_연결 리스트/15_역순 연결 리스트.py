from typing import List, Deque


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
# 풀이 1. 재귀 구조로 뒤집기
def reverseList_1(self, head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev:ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    
    return reverse(head)


# 풀이 2. 반복 구조로 뒤집기
def reverseList_2(self, head: ListNode) -> ListNode:
    node, prev = head, None
    
    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    
    return prev
    