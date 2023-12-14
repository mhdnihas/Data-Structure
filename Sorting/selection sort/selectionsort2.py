class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def __lt__(self, other):
        return self.grade<other.grade

def selection_sort(arr):
    for i in range(len(arr)):
        minimum=i
        for j in range(i+1,len(arr)):
            if arr[minimum]>arr[j]:
                minimum=j
        arr[i],arr[minimum]=arr[minimum],arr[i]





student1=Student("nihas",14,55)
student2=Student("muhammed",12,65)
student3=Student("Ali",13,45)
student4=Student("shalik",12,75)
student5=Student("shabeer",14,85)
student6=Student("fathima",13,54)

print("\nSELELCTION SORT BASED ON GRADE\n")
school=[student1,student2,student3,student4,student5,student6]
print("before sorting:")

i=1
for student in school:
    print(f"{i}.{student.name}: age:{student.age}  grade:{student.grade}")
    i+=1

selection_sort(school)
print("\n\nafter sorting:")
i=1
for student in school:
    print(f"{i}.{student.name}: age:{student.age}  grade:{student.grade}")
    i+=1