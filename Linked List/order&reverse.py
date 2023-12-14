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
    def traversal(self):
        current=self.head
        while current:
            print(current.data,end="  ")
            current=current.next
    def reverse_traverse(self):
        current=self.head
        stack=[]
        while current:
            stack.append(current.data)
            current=current.next
        while stack:
            print(stack.pop(),end="  ")


link_list=Singly_LinkedList()
link_list.append(1)
link_list.append(2)
link_list.append(3)
link_list.append(4)
link_list.append(5)

print("print order:")
link_list.traversal()
print("\n\nprint reverse order:")
print(link_list.reverse_traverse())