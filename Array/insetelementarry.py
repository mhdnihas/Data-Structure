array=[1,2,3,4,4,5,6]
# 1.given(item,loc,k,UB),set k=UB
# 2.repeat step 3&4 while k>=loc
# 3.array[k+1]=array[k]
# 4.k--
# 5.array[loc]=item
# 6.stop
loc=3
item=5
k=len(array)-1
array.append(None)
while k>loc:
    array[k+1]=array[k]
    k -= 1
array[loc] = item
print(array)