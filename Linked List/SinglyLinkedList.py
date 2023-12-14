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
    def prepend(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node

    def delete(self,value):
        current=self.head
        if current.data==value:
            self.head=current.next
            return
        prev=None
        while current and current.data!=value:
            prev=current
            current=current.next
        if current:
            prev.next=current.next
        return
    def insert_after_node(self,prev,data):
        if not prev:
            print("previose node is not exist in the linked list:")
            return
        new_node=Node(data)
        new_node.next=prev.next
        prev.next = new_node

    def traversal(self):
        current=self.head
        while current:
            print(f"data:{current.data} Address: {current.next}")
            current=current.next
    def reverse_traverse(self):
        current=self.head
        stack=[]
        while current:
            stack.append(current.data)
            current=current.next
        while stack:
            print(stack.pop(),end=" ")


link_list=Singly_LinkedList()
link_list.append(1)
link_list.append(2)
link_list.append(3)
link_list.append(4)
link_list.append(5)
link_list.traversal()
print("1.insert a node at beggning\n2.insert node at after any node\n3.Remove any node\n4.traverse\n5.traverse as reverse\n6.Exit")
choice=int(input("\nEnter your choice:"))
while(choice!=6):
    if choice==1:
        data=input("Enter a data:")
        link_list.prepend(data)
    elif choice==2:
        data = input("Enter a data:")
        link_list.insert_after_node(link_list.head.next, data)
    elif choice == 3:
        data=input("Enter a node in the linked list to remove:")
        link_list.delete(data)
    elif choice==4:
        link_list.traversal()
    elif choice==5:
        print("traverse as reverse:")
        link_list.reverse_traverse()
    elif choice==6:
        print("\n\n\t you are exited!")
    else:
        print("\n\tInvalid choice!")

    choice=int(input("\nEnter your choice:"))