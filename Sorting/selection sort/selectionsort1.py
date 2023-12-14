def selection_sort(arr):
    for i in range(len(arr)):
        minimum=i
        for j in range(i+1,len(arr)):
            if arr[minimum]>arr[j]:
                minimum=j
        arr[i],arr[minimum]=arr[minimum],arr[i]

array=[2,3,1,5,2,6,7]
print("---SELECTION SORT---")
print("before sorting :")
print(array)
selection_sort(array)
print("\nafter sorting:")
print(array)


