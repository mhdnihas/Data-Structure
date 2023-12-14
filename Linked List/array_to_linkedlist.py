class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
def arry_to_linkedList(arr):
    if not arr:
        return None
    head=ListNode(arr[0])
    current=head
    for value in arr[1:]:
        current.next=ListNode(value)
        current=current.next
    return head
def print_linkedList(head):
    current=head
    while current:
        print(f"data: {current.data} Address:{current.next}")
        current=current.next

arr=[14,14,13,31]
print("\narray is :",arr)
print("\narray converted Linked list:")
linked_list=arry_to_linkedList(arr)
print_linkedList(linked_list)
