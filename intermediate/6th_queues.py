"""
    Queues -- data structure very similar to lists and sequences, there are some differences like very specific order
    how elements get into this list and out of this list
    why should we use queue?
"""

import queue

q = queue.Queue()

numbers = [10, 20, 40, 30, 50, 80, 89]
for number in numbers:
    q.put(number)

print(q.get())
print(q.get())

lifo = queue.LifoQueue()

lifo_numbers = [23, 34, 45, 46, 57, 6, 68, 56, 3234, 234]

for lifo_number in lifo_numbers:
    lifo.put(lifo_number)

print(lifo.get())
print(lifo.get())

priority = queue.PriorityQueue()
priority.put((2, "Hello world"))
priority.put((11, "99"))
priority.put((4, 7.4))
priority.put((213,True))

while not priority.empty():
    print(priority.get())