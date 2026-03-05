# Design Linked List
# Platform: LeetCode
class Node:
    def __init__(self, val):
        self.val=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None

    def get(self, index: int) -> int:
        if index<0:
            return -1
        curr=self.head
        i=0
        while i<index and curr:
            curr=curr.next
            i+=1
        if curr is not None:
            return curr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        temp=Node(val)
        if self.head is None:
            self.head=temp
            self.tail=temp
        else:
            temp.next=self.head
            self.head=temp
        
    def addAtTail(self, val: int) -> None:
        temp=Node(val)
        if self.head is None:
            self.head=self.tail=temp
        else:
            self.tail.next=temp
            self.tail=temp
        
    def addAtIndex(self, index: int, val: int) -> None:
        temp=Node(val) 
        if index == 0:
            self.addAtHead(val)
        elif self.head is None:
            return 
        else:
            current=self.head
            inde=0
            while inde<index-1 and current:
                current=current.next
                inde+=1
            if current and inde == index-1:
                temp.next=current.next
                current.next=temp
                if temp.next is None:
                    self.tail=temp
    
    def deleteAtIndex(self, index: int) -> None:
        if index<0:
            return 
        elif self.head is None:
            return 
        elif index==0:
            temp=self.head
            self.head=self.head.next
            if self.head is None:
                self.tail=None
        else:
            current=self.head
            ind=0
            while ind<index-1 and current.next:
                ind+=1
                current=current.next
            if current.next is None:
                return

            if current.next == self.tail:
                self.tail = current

            current.next = current.next.next
               

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

