class Graph:
    def __init__(self):
        self.graph={}
    def inserting(self,v,u):
        if v not in self.graph:
            self.graph[v]=[]
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    def deleiting(self,vertex):
        if vertex in self.graph:
            for neighbers in self.graph[vertex]:
                self.graph[neighbers].remove(vertex)


        del self.graph[vertex]
g=Graph()
g.inserting("A","B")
g.inserting("C","E")
g.inserting("A","C")
g.inserting("A","E")
g.inserting("B","D")
g.inserting("D","C")
for vertex,neighbers in g.graph.items():
    print(f"vertex:{vertex}  Neighbors:{neighbers}")
g.deleiting("E")
print("\nAfter Deleting Node E:")
for vertex,neighbers in g.graph.items():
    print(f"vertex:{vertex}  Neighbors:{neighbers}")