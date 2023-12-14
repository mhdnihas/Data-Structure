def bubbles_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
n=int(input("Enter the size of array:"))
print("enter the elements:")
array=[]
for i in range(n):
    num=int(input(""))
    array.append(num)
bubbles_sort(array)
print("sorted array:",array)