
def insertion_sort(arr, key):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        temp=arr[i]
        while j>=0 and key(arr[j])>key(temp):
            arr[j+1]=arr[j]
            j -= 1
        arr[j+1]=temp
    return arr


arr=[(300,"cherry"),(180,"apple"),(80,"grapes"),(55,"banana"),(60,"orange"),(140,"butter")]
key = lambda x: x[0]
print("before sorting give the fruit and it's price:")
print(arr)
print("\nafter sorting fruits price:")
print(insertion_sort(arr, key))