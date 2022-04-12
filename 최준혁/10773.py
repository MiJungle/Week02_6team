import sys

n = int(sys.stdin.readline())
sum = 0
stack = []

for _ in range(n):
  num = int(sys.stdin.readline())
  if num == 0:
    sum -= stack.pop()
  else:
    stack.append(num)
    sum += num

print(sum)
