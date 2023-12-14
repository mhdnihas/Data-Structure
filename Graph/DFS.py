def insert(u):
    if u in graph:
        print("Node is already present in the graph")
        return
    graph[u]=[]
def insert_edge(u,v):
    if u not in graph:
        graph[u]=[]
    if v not in graph:
        graph[v]=[]
    graph[v].append(u)
    graph[u].append(v)
def DFS(node,visited,graph):
    if node not in graph:
        print("Node is not present in the graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for x in graph[node]:
            DFS(x,visited,graph)



graph={}
visited=set()
insert("A")
insert("B")
insert("C")
insert_edge("A","B")
insert_edge("A","D")
insert_edge("C","E")
insert_edge("C","A")
insert_edge("E","B")
insert_edge("M","A")
insert_edge("P","E")
print(graph)
print("\nDSF\n")
DFS("C",visited,graph)