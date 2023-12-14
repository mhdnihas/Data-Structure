def has_duplicate(arr):
    seen=set()
    for i in arr:
        if i in seen:
            return True
        seen.add(i)
    return False
array1=[1,2,1,4,5,6]
array2=[1,2,3]
print("has array1 duplicate value?", has_duplicate(array1))
print("has array2 duplicate value?", has_duplicate(array2))