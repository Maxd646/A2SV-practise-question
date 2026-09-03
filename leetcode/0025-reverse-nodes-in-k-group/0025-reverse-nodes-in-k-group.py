# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        ans = []
        curr = head

        while curr:

            ans.append(curr.val)
            curr = curr.next

        rever = []

        for i in range(0, len(ans)-k+1, k):

            rever.extend(ans[i:k+i][::-1])

        if i +k < len(ans):
            rever.extend(ans[i+k:])
        
        curr = ListNode(rever[0])
        head = curr
        i = 1

        while i < len(rever):

            curr.next = ListNode(rever[i])
            curr = curr.next

            i += 1

        return head

    

        
            
        