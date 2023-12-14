def check_balace(expression):
    stack=[]
    open_paranthesis=["{","(","["]
    closed_paranthesis={"}":"{",")":"(","]":"["}
    for char in expression:
        if char in open_paranthesis:
            stack.append(char)     #{
        else:
            if char in closed_paranthesis:
                if not stack or stack.pop()!=closed_paranthesis[char]:
                    return False
    return not stack
print("\n\t Using stack to check whether given expression is balanced or not")
expression1="[{()}]"
expression2="[}{()]"
expression3="[{}()]"
expression4="{[2]}"
print(f"\nis {expression1} balanced?  {check_balace(expression1)} \n")
print(f"is {expression2} balanced?  {check_balace(expression2)}\n ")
print(f"is {expression3} balanced?  {check_balace(expression3)} \n")
print(f"is {expression4} balanced?  {check_balace(expression4)} \n")
