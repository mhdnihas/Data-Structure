def sum_of_digit(num):
    if num<=0:
        return 0
    return num%10+sum_of_digit(num//10)
choice="y"
while choice=="y"or choice=="Y":
    n=int(input("Enter a number to find sum of its digit:"))
    print(f"sum of digit is :{sum_of_digit(n)}")
    choice=input("Do you want to try again(Y/N):")
    print("\n")
