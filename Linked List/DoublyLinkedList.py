class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doubly_linkedLis:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
            new_node.prev=current
    def delete(self,value):
        current=self.head
        while current:
            if current.data==value:
                if current.prev:
                    current.prev.next=current.next
                else:
                    self.head=current.next
                if current.next:
                    current.next.prev=current.prev
                elif current.prev:
                    current.prev.next=None
                return
            current=current.next

    def traverse(self):
        if not self.head:
            return
        current=self.head
        while current:
            print(f"Data:{current.data}bck:{current.prev}forw:{current.next}")
            current=current.next
    def retravers(self):
        current=self.head
        while current and current.next:
            current=current.next
        while current:
            print(current.data,end=" ")
            current=current.prev

linked_list=Doubly_linkedLis()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
print("Doubly linked list:")
linked_list.traverse()
print("\nafter delelte data(4):")
linked_list.delete(4)
linked_list.traverse()
print("\nreverse Doubly linked list:")
linked_list.retravers()


