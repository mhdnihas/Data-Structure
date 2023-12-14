import queue
myqueue=queue.Queue()
myqueue.put(1)
print("after adding:",list(myqueue.queue))
myqueue.put(2)
print("after adding:",list(myqueue.queue))

myqueue.put(3)
print("after adding:",list(myqueue.queue))



print(list(myqueue.queue))
print("after removing:",myqueue.get())
print(list(myqueue.queue))

print("after removing:",myqueue.get())
print(list(myqueue.queue))
