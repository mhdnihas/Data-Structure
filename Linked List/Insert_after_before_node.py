class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Singly_LinkedList:
    def __init__(self):
        self.head=None
    def append(self,value):

        new_node=Node(value)
        if not self.head:
            self.head=new_node
            return

        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

    def traverse(self):
        current =self.head
        while current:
            print(f"Data:  {current.data}    Address: {current.next}")
            current = current.next

    def insert_after(self,target,value):
        new_node=Node(value)
        current=self.head
        while current and current.data!=target:
            current=current.next
        new_node.next=current.next
        current.next=new_node
    def insert_before(self,target,value):
        new_node=Node(value)
        current=self.head
        prev=None
        while current and current.data!=target:
            prev=current
            current=current.next
        if prev:
            new_node.next=current
            prev.next=new_node
        else:
            new_node.next=current
            self.head=new_node




link_list=Singly_LinkedList()
link_list.append(1)
link_list.append(2)
link_list.append(3)
link_list.append(4)
link_list.append(5)
link_list.traverse()
value=4
print(f"\ninsert a number after{value}:")
link_list.insert_after(4,4.5)
link_list.traverse()
print(f"\ninsert a number before{value}:")

link_list.insert_before(4,3.5)
link_list.traverse()