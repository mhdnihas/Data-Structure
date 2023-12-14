array=[10,20,30,40,50,60,70,80]
beg=0
end=len(array)-1
item=int(input("Enter the Item:"))
mid=int((beg+end)/2)
while array[mid]!=item and beg<end:
    if item<array[mid]:
        end=mid-1
    else:
        beg=mid+1
    mid = int((beg + end) / 2)

if array[mid]==item:
    loc=mid+1
    print(f"{item} is found at {loc}")
else:
    loc=None
    print("item is not found")

