def heapify(arr,N,i):
    smallest=i
    l=2*i+1
    r=2*i+2
    if l<N and arr[l]<arr[smallest]:
        smallest=l
    if r<N and arr[r]<arr[smallest]:
        smallest=r

    if i!=smallest:
        arr[smallest],arr[i]=arr[i],arr[smallest]
        heapify(arr,N,smallest)
def build(arr,N):
    startidx=(N//2)-1
    for i in range(startidx,-1,-1):
        heapify(arr,N,i)

arr=[4,4,3,7,3,7,5,2]
print("BUILDING HEAP FROM GIVEN LIST")
print("given list is :",arr)

build(arr,len(arr))
print("\nuilt the heap:",arr)
