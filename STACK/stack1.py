stack=[]
def push():

    value = int(input("Enter a value to insert into stack:"))
    if len(stack)<limit:

        stack.append(value)

        print(stack)
    else:
        print("stack is underflow")

def pop():
    if len(stack) < 1:
        print("stack underflow")
    else:
        print("removed value is :",stack[-1])
        stack.pop()

        print(stack)
print("\tSTACK\t")
limit=int(input("enter the size of stack:"))
print("\n1.push\n2.pop\n3.quit")
while True:
    choice=int(input("enter your choice:"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break