
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        temp=arr[i]
        while arr[j]>temp and j>=0:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    return arr


arr=[5,4,8,6,10,7]
print("before sorting:")
print(arr)
print("\nafter sorting:")
print(insertion_sort(arr))