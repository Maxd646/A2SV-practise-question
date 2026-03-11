# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q=deque()
        curr=head
        while curr:
            while q and q[-1].val<curr.val:
                q.pop()
            q.append(curr)
            curr=curr.next
        head=q[0]
        curr=head
        i=1
        while i<len(q):
            curr.next=q[i]
            curr=curr.next
            i+=1
        curr.next=None
        return head

        
       
            



        