class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,value):

        new_node=Node(value)
        if not self.head:
            self.head=new_node
            return
        current = self.head
        while current.next:
            current=current.next
        current.next=new_node
    def prepend(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
    def traverse(self):
        current=self.head
        print("\n")
        while current:
            print(f"Data:{current.data} Address:{current.next}")
            current=current.next
linked_list=LinkedList()
print("we have a linked list:")
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.traverse()

data=input("\nEnter a data to add to linked list as last node:")
linked_list.append(data)
linked_list.traverse()
data=input("\nEnter a data to add to linked list as first node:")
linked_list.prepend(data)
linked_list.traverse()

