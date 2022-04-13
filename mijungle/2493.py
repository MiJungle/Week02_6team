import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
n = list(map(int, input().split()))
print(N,n)

d= n[-1]

while len(n) != 1:
    for i in range(len(n)-2, -1, -1 ):
        if d < n[i]:
            print(n[i])
            n.pop()
            d= n[-1]
            print(d)
    # else:
    #     print(0)
