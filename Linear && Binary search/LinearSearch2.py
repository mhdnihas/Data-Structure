def LinearSearch(arr,target):
    for i,element in enumerate(arr):
        if element==target:
            return i+1
    return -1
Fruits=["apple","grapes","banana","orange","painaple"]
str1=input("enter the fruit to search:")
loc=LinearSearch(Fruits,str1)
if loc!=-1:
    print(f"{str1} is found at {loc} in the array")
else:
    print(f"{str1} is not found")

