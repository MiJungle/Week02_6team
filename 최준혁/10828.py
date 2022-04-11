import sys
n = int(input())
mylist = []

for _ in range(n):
  myinput = sys.stdin.readline().split()

  if myinput[0] == "push":
    n = myinput[1]
    mylist.append(n)
  elif myinput[0] == "pop":
    if len(mylist) == 0:
      print(-1)
    else:
      print(mylist.pop())
  elif myinput[0] == "size":
    print(len(mylist))
  elif myinput[0] == "empty":
    if len(mylist) == 0:
      print(1)
    else:
      print(0)
  else:
    if len(mylist) == 0:
      print(-1)
    else:
      print(mylist[len(mylist) - 1])
    
