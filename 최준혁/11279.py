import sys
import heapq
n = int(sys.stdin.readline())
mylist = []

for _ in range(n):
  num = int(sys.stdin.readline())

  if num == 0:
    if len(mylist) == 0:
      print(0)
    else:
      print(heapq.heappop(mylist)[1])
  else:
    heapq.heappush(mylist, (-num, num))
