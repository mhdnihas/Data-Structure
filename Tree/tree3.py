class ExpressionNode:
    def __init__(self, value):
        self.value = value
        self.children = []


root = ExpressionNode("*")
root.children.append(ExpressionNode("+"))
root.children[0].children.append(ExpressionNode("2"))
root.children[0].children.append(ExpressionNode("3"))
root.children.append(ExpressionNode("4"))