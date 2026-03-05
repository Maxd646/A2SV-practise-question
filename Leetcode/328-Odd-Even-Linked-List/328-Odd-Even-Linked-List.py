# Odd Even Linked List
def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        ohead = otail = head
        ehead = etail = head.next

        current = head.next.next
        idx = 3 

        while current:
            if idx % 2 == 1:
                otail.next = current
                otail = otail.next
            else:
                etail.next = current
                etail = etail.next
            current = current.next
            idx += 1
        otail.next = ehead
        etail.next = None
        return head

