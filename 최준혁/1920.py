def binarySort(i, j, num):
  global arr
  center = (j + i) // 2
  # print(center,i,j)
  if i > j:
    return 0
    
  if arr[center] == num:
    return 1 
  elif arr[center] > num:
    return binarySort(i, center - 1, num)
  else:
    return binarySort(center + 1, j, num)
arr = []
n = int(input())
narr = list(map(int,input().split()))
m = int(input())
marr = list(map(int,input().split()))
arr = sorted(narr)
# print(sorted(narr))
for i in range(m):
  print(binarySort(0, n - 1, marr[i]))
