from typing import List, Deque


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 풀이 1. 리스트 변환
def isPalindrome_1(self, head: ListNode) -> bool:
    q: List = []
    
    if not head:
        return True
    
    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next
    
    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    
    return True


# 풀이 2. 데크를 이용한 최적화
import collections


def isPalindrome_2(self, head: ListNode) -> bool:
    # 데크 자료형 선언
    q: Deque = collections.deque()
    
    if not head:
        return True
    
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    
    return True


# 풀이 3. 고(Go)를 이용한 데크 구현


# 풀이 4. 런너를 이용한 우아한 풀이
def isPalindrome_4(self, head: ListNode) -> bool:
    rev = None
    slow = fast = head
    # 런너를 이용해 역순 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
        
    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    
    return not rev