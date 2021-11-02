from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        result_tail = result
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next


if __name__ == "__main__":
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    # 8, 9, 9, 9, 0, 0, 0, 1]
    solution = Solution()
    print(solution.addTwoNumbers(l1, l2))
