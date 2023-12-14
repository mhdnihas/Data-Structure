class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def remove_duplicate(head):
    current=head
    while current.next:
        if current.data==current.next.data:
            current.next=current.next.next
        else:
            current=current.next
def traverse(head):
    current=head
    while current:
        print(f"{current.data}-->",end="")
        current=current.next
linked_list=Node(1)
linked_list.next=Node(1)
linked_list.next.next=Node(2)
linked_list.next.next.next=Node(3)
linked_list.next.next.next.next=Node(3)
linked_list.next.next.next.next.next=Node(4)
print("before delete duplicate:")
traverse(linked_list)
print("\n\nAfter remove duplicate:")
remove_duplicate(linked_list)
traverse(linked_list)

