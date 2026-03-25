# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        ans = []
        curr = head
        while curr:
            ans.append(curr.val)
            curr = curr.next
        ans.sort()
        head = ListNode(ans[0])
        curr= head
        for i in range(1, len(ans)):
            curr.next=ListNode(ans[i])
            curr=curr.next
        return head