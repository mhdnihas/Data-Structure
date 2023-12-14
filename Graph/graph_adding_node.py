class Graph:
    def __init__(self):
        self.graph={}
    def addnode(self,node):
        if node in self.graph:
            print(f"{node} is alreadt present in the graph")
            return
        self.graph[node]=[]
    def addedge(self,v,u):
        if v not in self.graph:
            self.graph[v]=[]
        if u not in self.graph:
            self.graph[u]=[]

        self.graph[u].append(v)
        self.graph[v].append(u)
g=Graph()
g.addedge(2,3)
g.addedge(2,4)
g.addedge(4,3)
g.addedge(4,6)
for vetex,neighber in g.graph.items():
    print(f"node:{vetex},neighber:{neighber}")