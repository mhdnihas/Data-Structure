def merge_sort(arr):

    if len(arr)>1:
        mid=len(arr)//2
        left_side=arr[:mid]
        right_side=arr[mid:]
        # print(left_side,end="        ")
        # print(right_side)
        merge_sort(left_side)
        merge_sort(right_side)

        i,j,k=0,0,0
        while i<len(left_side) and j<len(right_side):
            if left_side[i]<right_side[j]:
                arr[k]=left_side[i]
                k+=1
                i+=1
            else:
                arr[k] =right_side[i]
                k += 1
                j +=1
        while j<len(right_side):
            arr[k] = right_side[j]
            k += 1
            j +=1
        while i < len(left_side):
            arr[k] = left_side[i]
            k += 1
            i+=1

    return arr

print("\tMERGE SORT\n")
array=[3,4,5,2,5,3,7,4,8,3,5]
print("\nbefore sorting:")
print(array)
print("\n after sorting:")
print(merge_sort(array))
