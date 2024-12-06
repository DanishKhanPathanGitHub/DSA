from queue import SimpleQueue

q1 = SimpleQueue()
q1.put(1)
q1.put(2)
q1.put(3)
print(q1)

print(q1.get())
print(q1.get())
print(q1.get())
print(q1)


