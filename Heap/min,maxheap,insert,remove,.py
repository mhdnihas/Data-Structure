class Minheap:
    def __init__(self):
        self.heap=[]
    def built_heap(self,arr):
        self.heap=arr[:]
        n=len(arr)
        startidx=n//2-1
        for i in range(startidx,-1,-1):
            self.heapify(i)
    def heapify(self,i):
        smallest=i
        l=2*i+1
        r=2*i+2
        if l<len(self.heap) and self.heap[smallest]>self.heap[l]:
            smallest=l
        if r<len(self.heap) and self.heap[smallest]>self.heap[r]:
            smallest=r
        if i!=smallest:
            self.heap[smallest],self.heap[i]=self.heap[i],self.heap[smallest]
            self.heapify(smallest)
    def remove_min(self):
        min_val=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify(0)
        return min_val

    def insert(self,value):
        self.heap.append(value)
        self.heap_up(len(self.heap)-1)
    def heap_up(self,i):
        while i>0:

            parent=(i-1)//2
            if self.heap[parent]>self.heap[i]:
                self.heap[i],self.heap[parent]=self.heap[parent],self.heap[i]
                i=parent
            else:
                break




arr=[5,8,3,4,1,3]
print("\n\tBUILDING MIN HEAP")
Min_heap=Minheap()
Min_heap.built_heap(arr)
print(Min_heap.heap)

print("removed minimum value in the Tree:",Min_heap.remove_min())
print(Min_heap.heap)
value=int(input("Enter a value to insert into heap:"))
Min_heap.insert(value)
print(f"After inserting {value} Min heap is:")
print(Min_heap.heap)

