def Bainary_Recursive(array,beg,end,target):
    mid = (beg + end) // 2
    while array[mid]!=item and beg<end:
        if target<array[mid]:
            return Bainary_Recursive(array,beg,mid-1,target)
        else:
            return Bainary_Recursive(array,mid+1,end, target)


    if array[mid]==target:
        loc=mid+1
        print(f"{target} is found at {loc}")
    else:
        loc=None
        print(f"{target} is not found")

array=[10,20,30,40,50,60,70,80]
beg=0
end=len(array)-1
print("array:",array)
item=int(input("Enter the Item:"))
Bainary_Recursive(array,beg,end,item)