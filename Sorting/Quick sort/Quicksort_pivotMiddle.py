def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quick_sort(left)+middle+quick_sort(right)
array=[64,34,25,22,90,30,22,44]
print("Quick sort using middle :\n")
print("before sorting:")
print(array)
print("\nafter sorting:")
print(quick_sort(array))