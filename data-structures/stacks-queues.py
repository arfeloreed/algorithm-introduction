# stack example
# stack = []

# add items to stack, e.g. 1, 2, 3, 4
# for i in range(1, 5):
#     stack.append(i)

# print stack
# print(stack)

# remove last item from stack
# x = stack.pop()
# print(x)
# print(stack)

# queue example
from collections import deque

# create an empty queue
queue = deque()

# add items to queue, e.g. 1, 2, 3, 4
for i in range(1, 5):
    queue.append(i)

# print queue
print(queue)

# remove first item from queue
x = queue.popleft()
print(x)
print(queue)