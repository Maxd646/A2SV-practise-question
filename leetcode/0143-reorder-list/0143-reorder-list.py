# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr= curr.next
        ans = []
        n = len(stack)-1
        for i in range((len(stack))//2):
            ans.append(stack[i])
            ans.append(stack[n-i])
        if len(stack)%2!=0:
            ans.append(stack[n//2])

        curr = head
        for val in ans:
            curr.val = val
            curr = curr.next
       
        
        