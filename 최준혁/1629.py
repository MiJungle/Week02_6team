def divideconquer(a, b):
  global c
  
  if b == 1:
    return a % c

  val = divideconquer(a, b // 2)
  
  if b % 2 == 0:
    return (val * val) % c
  else:
    return (val * val * a) % c
  
myarr = []
a,b,c = list(map(int, input().split()))
arr = []

print(divideconquer(a, b))
