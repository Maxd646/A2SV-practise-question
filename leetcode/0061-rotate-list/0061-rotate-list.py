# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head
        k = k % length
        newtail = length - k

        newTail = head
        for _ in range(newtail - 1):
            newTail = newTail.next

        newHead = newTail.next
        newTail.next = None

        return newHead
