import os
import subprocess

def slugify(text):
    return text.strip().replace(" ", "-")

def create_files(base, folder, filename, title, platform):
    path = os.path.join(base, folder)
    os.makedirs(path, exist_ok=True)

    # ---- Solution template ----
    solution_template = f"""# {title}
# Platform: {platform}
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

"""

    # ---- README template ----
    readme_template = f"""# {title}

## Platform
{platform}
## 707. Design Linked List

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.


## problem link:https://leetcode.com/problems/design-linked-list/description/
"""

    # ---- NOTES template ----
    notes_template = "# Notes\n\n- Observations\n- Mistakes\n"

    #  Write files with UTF-8 encoding
    with open(os.path.join(path, f"{filename}.py"), "w", encoding="utf-8") as f:
        f.write(solution_template)

    with open(os.path.join(path, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_template)

    with open(os.path.join(path, "NOTES.md"), "w", encoding="utf-8") as f:
        f.write(notes_template)

    print(" Created:", path)

    # --- Open VS Code automatically ---
    try:
        subprocess.run(["code", path])
    except:
        print(" VS Code not found in PATH, open manually")

# ------------------------
# MAIN
# ------------------------
platform = input("Platform (leetcode/codeforces/hackerrank/gfg): ").lower()

number = ""
if platform == "leetcode":
    number = input("Problem number: ")
    title = input("Title: ")
    folder = f"{number}-{slugify(title)}"
    create_files("LeetCode", folder, folder, title, "LeetCode")

elif platform == "codeforces":
    title = input("Title: ")
    name = slugify(title)
    folder = f"codeforces-{name}"
    create_files("Codeforces", folder, folder, title, "Codeforces")

elif platform == "hackerrank":
    title = input("Title: ")
    name = slugify(title)
    folder = f"hacker-rank-{name}"
    create_files("HackerRank", folder, folder, title, "HackerRank")

elif platform in ["gfg", "geeksforgeeks"]:
    title = input("Title: ")
    name = slugify(title)
    folder = f"geeksforgeeks-{name}"
    create_files("GeeksforGeeks", folder, folder, title, "GeeksforGeeks")

else:
    print(" Unknown platform")
