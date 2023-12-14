def fibanacci(n):
    if n<=1:
        return n
    else:
        return fibanacci(n-1)+fibanacci(n-2)

choice="y"
while choice=="y"or choice=="Y":
    n=int(input("Enter the range of fibanacci sieries:"))
    print("fibanacci series:")
    for i in range(n):
        print(fibanacci(i),end="  ")
    choice=input("\ndo you want to continue(y/n):")
    print("\n")
