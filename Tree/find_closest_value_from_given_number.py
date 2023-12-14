class BST:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def preorder(self):
        if self:
            print(self.value,end=" ")
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
def closest_value(root,target):
    closest=root.value
    while root:
        if abs(closest-target)>abs(root.value-target):
            closest=root.value
        if target<root.value:
            root=root.left
        elif target>root.value:
            root=root.right
        else:
            closest=root.value
            break

    return closest

tree=BST(20)
tree.left=BST(10)
tree.left.left=BST(5)
tree.left.left.left=BST(3)
tree.left.left.right=BST(7)
tree.right=BST(50)
tree.right.left=BST(25)
tree.right.right=BST(52)
while True:
    choice=int(input("\nSelect:\t1.find closet value \t2.preorder \t 3.Quit\nEnter Your Choice:"))
    if choice==1:
        item=int(input("Enter a item to find its closest value in the Tree:"))
        closest=closest_value(tree,item)
        print(f"closest value of {item}  in the Tree is :",closest)
    elif choice==2:
        print("preorder:")
        tree.preorder()
    elif choice==3:
        print("Exit")
        break
    else:
        print("\t Invalid Choice")



