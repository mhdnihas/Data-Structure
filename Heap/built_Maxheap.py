def heapify(arr,N,i):
    large=i
    r=2*i+1
    l=2*i+2
    if l<N and arr[l]>arr[large]:
        large=l
    if r<N and arr[r]>arr[large]:
        large=r

    if i!=large:
        arr[large],arr[i]=arr[i],arr[large]
        heapify(arr,N,large)
def build(arr,N):
    startidx=N//2-1
    for i in range(startidx,-1,-1):
        heapify(arr,N,i)
print("BUILT MAX HEAP FROM LIST")
arr=[1,3,5,4,6,13,10,9,8,15,17]
print("The given list is:",arr)
print("built heap:")
build(arr,len(arr))

print(arr)