# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        ans  = []

        curr = head
        
        while curr:

            ans.append(curr.val)
            curr = curr.next

        ans[k-1], ans[-k] = ans[-k], ans[k-1]
        head = ListNode(ans[0]) 
        i = 1
        curr = head
    
        while i < len(ans):

            curr.next = ListNode(ans[i])
            curr = curr.next
            i += 1
            
        return head

      
        