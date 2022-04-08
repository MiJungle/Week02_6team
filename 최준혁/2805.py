def binarySortver2(i, j, num):
  global arr
  global min
  global n
  if n == 1:
    return j - m
  center = (j + i) // 2
  if min > center:
    min = center
    # print('min:',min)
  # print(center,i,j)
  sum = 0
  for k in range(n):
    if arr[k] - center > 0:
      sum += arr[k] - center
  # print('sum:',sum)
  if i > j:
    if sum > num:
      # print('a')
      return center
    else:
      return center - 1
  if sum == num:
    # print('c')
    return center 
  elif sum < num:
    # print('d')
    return binarySortver2(i, center - 1, num)
  else:
    # print('e')
    return binarySortver2(center + 1, j, num)

min = 1000000001
arr = []
n, m = list(map(int,input().split()))
# print(n, m)
arr = list(map(int,input().split()))
# print(arr)
arr.sort()
print(binarySortver2(0, arr[n-1], m))
