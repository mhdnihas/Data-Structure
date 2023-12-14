def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left_side=arr[:mid]
        right_side=arr[mid:]
        merge_sort(left_side)
        merge_sort(right_side)

        i,j,k=0,0,0
        while i<len(left_side) and j<len(right_side):
            if left_side[i][0]<right_side[j][0]:
                arr[k]=left_side[i]
                i+=1
                k+=1
            else:
                arr[k] = right_side[j]
                j += 1
                k += 1
        while i < len(left_side):
            arr[k] = left_side[i]
            i += 1
            k += 1
        while j<len(right_side):
            arr[k] = right_side[j]
            j += 1
            k += 1

print("\nMERGE SORT BASED ON ROLLNO")
array=[(3,"nihas"),(1,"shalik"),(5,"sinan"),(6,"shahzad"),(2,"muhammed"),(4,"faijas")]
print("before sorting:")
print(array)
print("\nafter sorting :")
merge_sort(array)
print(array)