array=["apple", "banana", "cherry", "date"]
beg=0
end=len(array)-1
item=input("Enter the Fruit name to search:")
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