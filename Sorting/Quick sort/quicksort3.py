class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

def partition(list1,first,last,key):

    pivot=key(list1[first])
    left=first+1
    right=last
    while True:

        while left<=right and pivot>=key(list1[left]):

            left+=1
        while left<=right and pivot<=key(list1[right]):

            right-=1
        if left>right:
            break
        list1[left],list1[right]=list1[right],list1[left]
    list1[first],list1[right]=list1[right],list1[first]
    return right

def quick_sort(list1,first,last,key):
    if first>=last:
        return
    p=partition(list1,first,last,key)
    quick_sort(list1,first,p-1,key)
    quick_sort(list1,p+1,last,key)



list1=[Person("nihas",21),Person("ali",18),Person("Rafi",21),Person("Muhammed",22),Person("shalik",19)]
print("Quick Sort Age wise:\n")
print("before sorting :")
for person in list1:
    print(f"{person.name} : {person.age}")
quick_sort(list1,0,4,lambda x:x.age)
print("\nafter sorting:")

for person in list1:
    print(f"{person.name} : {person.age}")