def LinearSearch(arr,target):
    for i,element in enumerate(arr):
        if target in element.values():
            return i+1
    return -1
student=[
    {"name":"nihas","age":21},
    {"name":"shalik","age":19},
    {"name":"ali","age":18},
    {"name":"Muhammed","age":22},
    {"name":"sabith","age":18},
   ]
select=input("Enter the student to search:")
result=LinearSearch(student,select)
if result!=-1:
    print(f"{select} is found at {result}")
else:
    print(f"{select} is not found")