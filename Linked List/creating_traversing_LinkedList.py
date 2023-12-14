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

        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

    def traversal(self):
        current=self.head
        while current:
            print(f"data:{current.data} Address: {current.next}")
            current=current.next
link_list=LinkedList()
link_list.append(1)
link_list.append(2)
link_list.append(3)
link_list.append(4)
link_list.append(5)


link_list.traversal()

