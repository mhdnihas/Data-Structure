
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


fruit=["apple","mango","orange","kiwi","pinaple","cocunut","grapes","banana"]
print("before sorting:")
print(fruit)
print("\nafter sorting:")
print(insertion_sort(fruit))
