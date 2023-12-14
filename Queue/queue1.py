queue=[]
def enqueue():
    item=int(input("Enter the item to be insert into the queue:"))
    queue.append(item)
def dequeue():
    item=queue.pop(0)
    print("removed the element is :",item)
def display():
    print(queue)


while True:
    print("YOU CAN SELECT THE OPERATIONS:\n1.INSERT\n2.Remove\n3.display\n4.quite")

    choice=int(input("Enter the choice:"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("\n\tPlease Enter correct choice")
