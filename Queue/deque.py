import collections
queue=collections.deque()

while True:
    print("Select choice:\n1.Insert at end\n2.Insert at beggning\n3.Remove at end\n4.Remove at beggning\n5.Display\n6.Quit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        item=int(input("Enter a element:"))
        queue.append(item)
    elif choice==2:
        item=int(input("Enter a element:"))
        queue.appendleft(item)
    elif choice==3:
        item=queue.pop()
        print("removed item is ",item)
    elif choice==4:
        item=queue.popleft()
        print("removed item is ",item)

    elif choice==5:
        lis=list[queue]
        print(lis)
    elif choice==6:
        break
    else:
        print("!Enter a valid number.")
