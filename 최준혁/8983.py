def binary():
  global shooter
  global animal
  global m, n, l
  cnt = 0
  
  for i in range(n):
    x = animal[i][0]
    y = animal[i][1]

    if y == l:
      if x in shooter:
        cnt += 1
        # print('check1')
    elif y > l:
      continue
    else:
      boundary = l - y
      fp = 0
      lp = m - 1
      while fp <= lp:
        mp = (fp + lp) // 2
        mid = shooter[mp]
        if x >= mid - boundary and x <= mid + boundary:
          cnt += 1
          # print('checkx',x,'i',i,'mid',mid,'boundary',boundary)
          break
        if x < mid - boundary:
          lp = mp - 1
        else:
          fp = mp + 1
 
  return cnt
          

m, n, l = list(map(int,input().split()))
# print(m,n,l)
shooter = []
shooter = list(map(int,input().split()))
shooter.sort()
# print(shooter)
animal = []
# print(shooter)
for i in range(n):
  animal.append(list(map(int,input().split())))

# print(animal)

print(binary())

