class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
def bubble_sort(people):
    n=len(people)
    for i in range(n):
        for j in range(n-i-1):
            if people[j].age>people[j+1].age:
                people[j],people[j+1]=people[j+1],people[j]

peoples=[person("Muhammed",33),person("suhair",19),person("nihas",21),person("Ali",20),person("shalik",20),person("faijas",22)]
print("\nsorted by age wise:\n")
bubble_sort(peoples)
for person in peoples:
    print(f"{person.name}:{person.age}")
