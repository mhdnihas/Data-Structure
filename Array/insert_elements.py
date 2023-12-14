def insert_element(array, element, index):
    new_array=[]
    for i in range(index):
        new_array.append(array[i])
    new_array.append(element)
    for i in range(index+1,len(array)):
        new_array.append(array[i])
    return new_array



array=[1,3,4,5,6]
print("before inseting :")
print(array)
print("after inserting:")
arr=insert_element(array,100,3)
print(arr)