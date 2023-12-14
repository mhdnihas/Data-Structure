class Tree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def valid_BST(node,min=0,max=1000):
    if node is None:
        return True
    if node.value<min or node.value>max:
        return False
    return valid_BST(node.left,min,node.value) and valid_BST(node.right,node.value,max)
print("\n\tCHECKING THE GIVEN TREE IS BST OR NOT\n")
tree=Tree(8)
tree.left=Tree(5)
tree.left.left=Tree(4)
tree.left.right=Tree(6)
tree.right=Tree(12)
tree.right.left=Tree(7)
tree.right.right=Tree(16)
print("is first tree is valid BST ?",valid_BST(tree))

tree2=Tree(10)
tree2.left=Tree(5)
tree2.right=Tree(20)
print("is second tree is valid BST?",valid_BST(tree2))