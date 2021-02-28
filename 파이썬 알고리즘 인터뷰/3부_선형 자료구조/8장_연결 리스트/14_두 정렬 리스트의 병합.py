class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 풀이 1. 재귀 구조로 연결
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1