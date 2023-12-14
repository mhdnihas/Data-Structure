array=[1,2,3,4,2,4,5,8]
n=len(array)
item=int(input("Enter the item to be search:"))
array.append(item)
loc=0
while array[loc]!=item:
    loc+=1
if loc==n:
    print("not found")
else:
    print(f"{item} is found at {loc+1}")