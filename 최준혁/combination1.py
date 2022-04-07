# import sys

# def recur(cnt, tempoutput, j):
#   global flag
#   global l
#   global output
#   global lim
  
#   if cnt == 6:
#     # tempoutput.sort()
#     mylist = tempoutput
    
#     if mylist not in output:
#       output.append(mylist)
#       for i in range(6):
#         if i == 5:
#           print(tempoutput[i], end='\n')
#         else:
#           print(tempoutput[i], end=' ')
#     return
    
#   for i in range(j, lim):
#     # print(cnt)
#     if flag[i] == 0:
#       flag[i] = 1
#       if cnt > 1 and tempoutput[cnt - 1] < tempoutput[cnt - 2]:
#         continue
#       copied = tempoutput.copy()
#       tempoutput.append(int(l[j + 1]))
#       recur(cnt + 1, tempoutput, j + 1)
#       flag[i] = 0
#       tempoutput = copied
# #   for i in range(j, lim):
# #     if flag[i] == 0:
      
# # myinput = []

# while ():
#   sys.stdin.readline().split()

# while (1):
#   l = []
#   tempoutput = []
#   output = []
#   l = input().split()
#   # print(l)
#   if int(l[0]) == 0 and len(l) == 1:
#     break
#   n = int(l[0])
#   lim = n
#   flag = [0] * n
#   idx = 0
#   recur(0, tempoutput, 0)
#   print()

# # from itertools import combinations


# # a = list(map(int, input().split()))

# # while a[0] != 0:
# #     k = a[0]
# #     list1 = list(combinations(a[1:],6))         # 입력받은 리스트의 0번째는 k 값 이므로 1번쨰 인덱스부터 숫자 6개를 뽑는 조합을 만듬
# #     for i in list1:                             # 해당 조합을 출력
# #         for j in i:
# #             print(j, end=' ')
# #         print()
# #     print()
# #     a = list(map(int, input().split())) 

## 조합 함수 구현
def myCombination(cnt, fr, t):
  global r
  global arr
  global counter
  if cnt == c:
      print(arr)
      counter += 1
      return
  for i in range(fr, t):
    arr[cnt] = i
    myCombination(cnt + 1, i + 1, t + 1)
    arr[cnt] = 0

counter = 0
myinput = input().split()
newArray = []
r = int(myinput[0])
## ex) 5개를 선택
c = 5
newArray = myinput[1:r+1]
print(myinput)
print(newArray)
arr = [0] * c
fr = 0
t = r - c + 1

myCombination(0, fr, t)
print(counter)
      
