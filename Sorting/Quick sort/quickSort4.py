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



friut=["banana","apple","stwabberry","grapes","kiwi","cherry","cocunut"]
last=len(friut)-1
print("Quick sort:\n")
print("before sorting :")
print(friut)
quick_sort(friut,0,last)
print("\nafter sorting:")
print(friut)