from collections import deque

# Using list as a queue
queue = []

# Enqueue
queue.append("a")
queue.append("b")
queue.append("c")

print("Initial queue")
print(queue)

# Dequeue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)


# ----------------------------------


# Initialize a deque
queue = deque()

# Enqueue
queue.append("a")
queue.append("b")
queue.append("c")

print("Initial queue")
print(queue)

# Dequeue
print("\nElements dequeued from the queue")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print("\nQueue after removing elements")
print(queue)
# queue.rotate(1)
print(queue)

# if queue:
print(queue[10])
