class Minstack:
    def __init__(self):
        self.stack=[]
        self.ministack=[]
    def push(self,item):
        self.stack.append(item)
        if not self.ministack or item<self.ministack[-1]:
            self.ministack.append(item)
    def pop(self):
        if self.stack:
            item=self.stack.pop()
            if item==self.ministack[-1]:
                self.ministack.pop()
        else:
            print("stack underflow")
    def getmin(self):
        if self.ministack:
            return self.ministack[-1]
stack=Minstack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(0)
print("\nFIND THE MINIMUM VALUE IN THE STACK")
print("\n",stack.stack,"\n")
print("now minimum value in the stack is:",stack.getmin())
item=stack.pop()
print("\nafter pop operation",stack.stack)
print("\nafter pop operation minimum value in the stack is:",stack.getmin())