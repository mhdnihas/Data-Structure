def partition(list1,first,last):

    pivot=list1[first]
    left=first+1
    right=last
    while True:

        while left<=right and pivot>=list1[left]:

            left+=1
        while left<=right and pivot<=list1[right]:

            right-=1
        if left>right:
            break
        list1[left],list1[right]=list1[right],list1[left]
    list1[first],list1[right]=list1[right],list1[first]
    return right

def quick_sort(list1,first,last):
    if first>=last:
        return
    p=partition(list1,first,last)
    quick_sort(list1,first,p-1)
    quick_sort(list1,p+1,last)



list1=[56,26,44,17,31,91]
print("Quick Sort:\n")
print("before sorting :")
print(list1)
quick_sort(list1,0,5)
print("\nafter sorting:")
print(list1)