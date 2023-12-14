class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


root = TreeNode("A")
root.children.append(TreeNode("B"))
root.children.append(TreeNode("C"))
root.children[0].children.append(TreeNode("D"))
root.children[0].children.append(TreeNode("E"))
root.children[1].children.append(TreeNode("F"))
print("root:",root.value)
