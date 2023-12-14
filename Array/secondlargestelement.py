def seconlaregest(arr):
    first=arr[0]
    second=arr[0]
    for i in arr:
        if first<i:
            second=first
            first=i
        if first>i>second:
            second=i
    return second
array1=[1,2,26,3,23,12]
array2=[0,2,15,3,23,19]
print("2nd largest from first array:",seconlaregest(array1))
print("2nd largest from second array:",seconlaregest(array2))

