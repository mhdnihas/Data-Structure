from collections import  deque
def BSF(graph,start):
    visited=set()
    queue=deque([start])
    visited.add(start)
    while queue:
        node=queue.popleft()
        print(node,end="  ")
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
graph={
    "A":["B","C"],
    "B":["D","E"],
    "C":["F","G"],
    "D":["B"],
    "E":["H","B"],
    "F":["C"],
    "G":["C"]
}
print("\nBreadth first Search\n")
BSF(graph,"A")