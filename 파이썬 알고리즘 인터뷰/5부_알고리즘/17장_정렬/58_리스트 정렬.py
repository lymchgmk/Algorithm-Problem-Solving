from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 풀이 1. 병합 정렬
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = self.mergeTwoLists(l1.next, l2)
        
    return l1 or l2


def sortList_1(self, head: ListNode) -> ListNode:
    if not (head and head.next):
        return head
    
    # 런너 기법 활용
    half, slow, fast = None, head, head
    while fast and fast.next:
        half, slow, fast = slow, slow.next, fast.next.next
    half.next = None
    
    # 분할 재귀 호출
    l1 = self.sortList(head)
    l2 = self.sortList(slow)
    
    return self.mergeTwoLists(l1, l2)


# 풀이 2. 퀵 정렬
# 로무토 파티션같은 일반적인 퀵 정렬 알고리즘으로 구현하면, 타임아웃이 발생해 풀이가 불가능하다.


# 풀이 3. 내장 함수를 이용하는 실용적인 방법
def sortList_3(self, head: ListNode) -> ListNode:
    # 연결 리스트 -> 파이썬 리스트
    p = head
    lst: List = []
    while p:
        lst.append(p.val)
        p = p.next
    
    # 정렬
    lst.sort()
    
    # 파이썬 리스트 -> 연결 리스트
    p = head
    for i in range(len(lst)):
        p.val = lst[i]
        p = p.next
    
    return head
