# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans1 = []
        curr = l1
        while curr:
            ans1.append(curr.val)
            curr=curr.next
        ans2 = []
        curr = l2
        while curr:
            ans2.append(curr.val)
            curr=curr.next
        an1 = 0

        for i in range(len(ans1)):
            an1 = 10*an1+ans1[i]

        an2=0

        for i in range(len(ans2)):
            an2 = 10*an2+ans2[i]

        total = str(an1+an2)
        head = ListNode(int(total[0]))
        curr = head

        for i in range(1, len(total)):
            curr.next = ListNode(int(total[i]))
            curr = curr.next

        return head


        
        
        