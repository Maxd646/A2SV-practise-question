# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        ans = []

        for head in lists:
            
            while head:

                ans.append(head.val)
                head = head.next

        ans.sort()

        if not ans:
            return None

        head =  ListNode(ans[0])
        curr = head
        curr.next = None
        i = 1

        while i<len(ans):

            curr.next  =  ListNode(ans[i])
            curr = curr.next 
            curr.next = None
            i += 1

        return head
        

        
        

        
        
        

        