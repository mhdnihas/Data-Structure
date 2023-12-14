def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

fruit=["apple","mango","orange","kiwi","pinaple","cocunut","grapes","banana"]
print("\n\t  Fruit descending order:\n\n\t",bubble_sort(fruit))