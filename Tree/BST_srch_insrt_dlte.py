class ListNode:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None
class BST:
    def __init__(self,data):
        self.root=ListNode(data)

    def insert(self,data):
        if self.root.key is None:
            self.root.key=data
        else:
            node=BST(data)
            self.insert_node(self.root,data)

    def insert_node(self,node,data):
        if node.key==data:
            return
        if node.key>data:
            if node.left is None:
                node.left=ListNode(data)
            else:
                self.insert_node(node.left,data)

        else:
            if node.right is None:
                node.right=ListNode(data)
            else:
                self.insert_node(node.right,data)
    def search(self,value):
        self.search_node(self.root,value)
    def search_node(self,node,value):
        if node.key==value:
            print(f"{value} is presents.")
            return
        if node.key>value:
            if node.left:
                self.search_node(node.left,value)
            else:
                print(f"{value} is not presents in the tree")
                return

        elif node.key<value:
            if node.right:
                 self.search_node(node.right,value)
            else:
                print(f"{value} is not present")
                return
    def preorder(self):
        self.preorder_node(self.root)

    def preorder_node(self,node):
        if node:
            print(node.key,end=" ")
            self.preorder_node(node.left)
            self.preorder_node(node.right)

    def inorder(self):
        self.inorder_node(self.root)
    def inorder_node(self,node):
        if node:

            self.inorder_node(node.left)
            print(node.key,end=" ")
            self.inorder_node(node.right)

    def postorder(self):
        self.postorder_node(self.root)
    def postorder_node(self,node):
        if node:

            self.postorder_node(node.left)
            self.postorder_node(node.right)
            print(node.key,end=" ")
    def delete(self,data):
        self.delete_node(self.root,data)


    def delete_node(self, node, data):
        if node is None:
            print(f"{data} is not present")
            return node

        if data < node.key:
            node.left = self.delete_node(node.left, data)
        elif data > node.key:
            node.right = self.delete_node(node.right, data)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            sub = node.right
            while sub.left:
                sub = sub.left
            node.key = sub.key
            node.right = self.delete_node(node.right, sub.key)

        return node


tree= BST(None)
bst=[21,30,10,12,5,25,100,3,7]

for i in bst:
    tree.insert(i)
while True:
    print("\nselect choice:\n1.insert\t  2.search\t3.traverse preorder\t   4.trverse Inorder\t5.traverse postorder\t 6.delete\t 7.Quite")
    choice=int(input("Enter your choice:"))
    if choice==1:
        n=int(input("Enter a number to insert:"))
        tree.insert(n)
    elif choice==2:
        item=int(input("Enter a item to be searched:"))
        tree.search(item)
    elif choice==3:
        print("\ntraverse preorder:")
        tree.preorder()
    elif choice==4:
        print("\ntraverse Inorder:")
        tree.inorder()
    elif choice==5:
        tree.postorder()
    elif choice==6:
        item=int(input("Enter a item to be deleted:"))
        tree.delete(item)
    elif choice==7:
        print("\n\n\t Exit")
        break
    else:
        print("Invalid choice")


#            21
#       10        30
#   5       12 25     100
# 3    7
