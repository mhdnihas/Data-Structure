import collections
import queue
# q=collections.deque()
# print(not q)
# q.append(3)
# q.append(3)
# q.append(5)
# q.pop()
# print(q[-1])

qu=queue.Queue()
qu.put(3)
qu.put(5)
qu.put(6)
qu.put(7)
print(qu.get())
print()
print()
