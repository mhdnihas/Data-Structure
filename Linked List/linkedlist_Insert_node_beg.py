class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def traverse(head):
    current=head
    while current:
        print(f"Data:  {current.data}    Address: {current.next}")
        current=current.next
def insert_begning(node,data):
    new_node=Node(data)
    new_node.next=node
    return new_node
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)
traverse(head)
head=insert_begning(head,0)
print("After inserting a node at beggning:")
traverse(head)