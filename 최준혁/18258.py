import sys
from collections import deque

n = int(sys.stdin.readline())
mylist = deque([])
inlist = []
for _ in range(n):
  inlist = sys.stdin.readline().split()

  if inlist[0] == 'push':
    mylist.append(inlist[1])
  elif inlist[0] == 'pop':
    if len(mylist) == 0:
      print(-1)
    else:
      print(mylist.popleft())
  elif inlist[0] == 'size':
    print(len(mylist))
  elif inlist[0] == 'empty':
    if len(mylist) == 0:
      print(1)
    else:
      print(0)
  elif inlist[0] == 'front':
    if len(mylist) == 0:
      print(-1)
    else:
      print(mylist[0])
  else:
    if len(mylist) == 0:
      print(-1)
    else:
      print(mylist[len(mylist) - 1])
    
