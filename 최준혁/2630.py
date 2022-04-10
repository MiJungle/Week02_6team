def mergesort(x1, x2, y1, y2, k):
  global arr
  global myarr
  global point
  
  if k == 1:
    if arr[x1][y1] == 0:
      point[0] += 1
      return 0
    else:
      point[1] += 1
      return 1
  else:
    # + 1 하는걸 깜빡
    part1 = mergesort(x1, (x1 + x2) // 2, y1, (y1 + y2) // 2, k // 2)
    part2 = mergesort(x1, (x1 + x2) // 2, ((y1 + y2) // 2) + 1, y2, k // 2)
    part3 = mergesort(((x1 + x2) // 2) + 1, x2, y1, (y1 + y2) // 2, k // 2)
    part4 = mergesort(((x1 + x2) // 2) + 1, x2, ((y1 + y2) // 2) + 1, y2, k // 2)
    # 네개다 -1일때 반례가 존재했음. 
    if part1 == part2 and part2 == part3 and part3 == part4 and part1 != -1:
      
      if arr[x1][y1] == 0:
        point[0] -= 3
        return 0
      else:
        point[1] -= 3
        return 1
    else:
      return -1

myarr = []
n = int(input())
arr = []
point = [0, 0]
for i in range(n):
  arr.append(list(map(int, input().split())))

mergesort(0, n - 1, 0, n - 1, n)
print(point[0])
print(point[1])
