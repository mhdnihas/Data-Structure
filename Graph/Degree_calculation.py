from  collections import defaultdict
def degree(graph,node):
    degree=0
    for x in graph[node]:
        degree+=1
    return degree
graph=defaultdict(list)
graph[1].append(4)
graph[2].append(4)
graph[1].append(3)
graph[5].append(3)
graph[1].append(6)
value1=1
value2=2
degree=degree(graph,value1)
print(f"\ndegree of {value1} is :",degree)


