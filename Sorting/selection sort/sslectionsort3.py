def selection_sort(arr):
    for i in range(len(arr)):
        minimum=i
        for j in range(i+1,len(arr)):
            if arr[minimum]>arr[j]:
                minimum=j
        arr[i],arr[minimum]=arr[minimum],arr[i]

array=["banana","apple","grapes","kiwi","cherry"]
print("---SELECTION SORT BASED ON STRING---")
print("before sorting :")
print(array)
selection_sort(array)
print("\nafter sorting:")
print(array)

