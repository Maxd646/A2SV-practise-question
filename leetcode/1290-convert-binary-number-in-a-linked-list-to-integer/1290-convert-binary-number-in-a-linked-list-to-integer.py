# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans= ""
        curr = head
        while curr:
            ans += str(curr.val)
            curr = curr.next
        return int(ans, 2)
        