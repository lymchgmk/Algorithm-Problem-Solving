# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, current, parts = 0, head, []

        while current:
            length += 1
            current = current.next

        base_size, extra = divmod(length, k)
        current = head

        for _ in range(k):
            dummy = ListNode()
            part_head = dummy

            for _ in range(base_size + (0 < extra)):
                dummy.next, current, dummy = current, current.next, current

            if 0 < extra:
                extra -= 1

            dummy.next = None
            parts.append(part_head.next)

        return parts
