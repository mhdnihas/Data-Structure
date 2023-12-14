class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def traverse(head):
    current=head
    while current:
        print(f"Data:  {current.data}    Address: {current.next}")
        current=current.next
def insert_begning(head,data,loc):
    new_node=Node(data)
    current=head
    i=1
    prev=None
    while new_node:
        if i==loc:
            if prev:
                prev.next=new_node
                new_node.next=current
                return head
            new_node.next = current
            return head
        i+=1
        prev=current
        current=current.next
    return head





head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)
traverse(head)
head=insert_begning(head,0,3)
print("After inserting a node at beggning:")
traverse(head)