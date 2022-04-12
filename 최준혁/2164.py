import sys
from collections import deque

n = int(sys.stdin.readline())
sum = 0
stack = []
queue = deque([])

for i in range(1, n + 1):
  queue.append(i)
  
while len(queue) > 1:
  queue.popleft()
  queue.append(queue.popleft())

print(queue[0])
