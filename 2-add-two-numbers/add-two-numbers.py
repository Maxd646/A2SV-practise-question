# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        curr = l1
        while curr:
            num1+=str(curr.val)
            curr= curr.next
        num2 = ""
        cur = l2
        while cur:
            num2+=str(cur.val)
            cur = cur.next
        total = str(int(num1[::-1])+int(num2[::-1]))[::-1]
        head = ListNode(0)
        curr  = head
        for i in range(len(total)):
            curr.next = ListNode(int(total[i]))
            curr = curr.next
        return head.next



        

        