def shift(arr,num):
    i,j=0,len(arr)-1
    while i<j:
        if arr[j]!=num:
            if arr[i]==num:
                arr[j],arr[i]=arr[i],arr[j]
                i+=1
                j-=1
            else:
                i+=1
        else:
            j-=1
array=[6,8,6,0,1,3,6,0,6]
shift(array,6)
print(array)