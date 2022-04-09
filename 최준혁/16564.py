def binary():
  global lv
  global m, n
  global arr
  fp = 0 #min(lv)
  lp = n #min(lv) + n
  minval = min(lv)
  #리스트 만들면 메모리 초과
  out = minval + 1
  
  while fp <= lp:
    mp = (fp + lp) // 2
    sum = 0
    center = minval + mp
    for i in range(m):
      if center > lv[i]:
        sum += (center - lv[i])
    if sum == n:
      out = center
      # print('1', i, out, sum, mp, fp, lp)
      break
    if sum > n:
      lp = mp - 1
      # print('2', i, out, sum, mp, fp, lp)
    else:
      fp = mp + 1
      out = center
      # print('3', i, out, sum, mp, fp, lp)
      
  return out
          

m, n = list(map(int,input().split()))
lv = []
for i in range(m):
  lv.append(int(input()))

lv.sort()
print(binary())

