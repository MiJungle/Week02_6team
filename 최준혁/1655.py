import sys
from collections import deque
import heapq

n = int(sys.stdin.readline())
sum = 0
stack = []
queue = deque([])
heap = []

for _ in range(n):
  num = int(sys.stdin.readline())
  heapq.heappush(heap, num)


sum = 0
if n == 1:
  print(0)
elif n == 2:
  for _ in range(n):
    sum += heapq.heappop(heap)
  print(sum)
else:
  for i in range(n):
    if i == 0:
      sum += heapq.heappop(heap)
    elif i == 1:
      sum += heapq.heappop(heap)
      heapq.heappush(heap, sum)
    else:
      temp = heapq.heappop(heap) + heapq.heappop(heap)
      sum += temp
      heapq.heappush(heap, temp)
  print(sum)
