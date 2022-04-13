import sys
# from collections import deque
# import heapq

n = int(sys.stdin.readline())
mylist = []

mylist = list(map(int, sys.stdin.readline().split()))
mylist.sort()
min = 2000000001

leftsol = 0
rightsol = 0

for i in range(n - 1):
  temp = mylist[i]
  lp = i + 1
  rp = len(mylist) - 1
  while lp <= rp:
    mid = (lp + rp) // 2
    sum = temp + mylist[mid]
    if sum == 0:
      min = sum
      leftsol = mylist[i]
      rightsol = mylist[mid]
      break
    elif sum > 0:
      if abs(sum) < abs(min):
        min = sum
        leftsol = mylist[i]
        rightsol = mylist[mid]
      rp = mid - 1
    else:
      if abs(sum) < abs(min):
        min = sum
        leftsol = mylist[i]
        rightsol = mylist[mid]
      lp = mid + 1
      
print(leftsol, rightsol)
