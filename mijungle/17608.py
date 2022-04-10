import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())

M = [int(input().rstrip()) for _ in range(N)]
count = 1
for i in range(len(M)-2, -1, -1 ):
    d = M[-1]
    if d < M[i]:
        d = M[i]
        count+=1
        print(d)
print(count)


