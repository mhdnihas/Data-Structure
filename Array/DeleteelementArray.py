# 1.given(loc,UB,LB,array),set k=loc,item=array[loc]
# 2Repeat step 3 & 4 while k<UB
# 3.array[k]=array[k+1]
# 4.k++
# 5.stop
array=[1,2,3,4,4,5,6]
k=3
item=array[k]

print("Item:",item)
while(k<len(array)-1):
    array[k]=array[k+1]
    k+=1
array.pop()
print(array)
