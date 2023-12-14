class Tree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def find_height(obj):
    if obj is None:
        return -1
    left=find_height(obj.left)
    right=find_height(obj.right)
    return max(left,right)+1
def display(obj1):
    if obj1 is None:
        return
    print(obj1.value)
    display(obj1.left)
    display(obj1.right)

obj=Tree(10)
obj.left=Tree(20)
obj.right=Tree(30)
obj.left.left=Tree(40)
obj.left.right=Tree(50)
obj.right.left=Tree(60)
print(f"heght={find_height(obj)}")
display(obj)