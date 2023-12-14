def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

choice='y'
while choice=='y' or choice=='Y':
    n=int(input("enter a number:"))
    print(f"Factorial of {n} is : {factorial(n)}")
    choice=input("do you want to calculate factorial?(Y/N):")
    print("\n")