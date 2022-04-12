import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

m = 1
S = []

while m != 0:
    m = list(map(int, input().split()))
    S.append(m)
    if m == [0]:
        break
# print(S)

def square():
    for s in S:
        d = s.pop(-1)
        m = s.pop(-1)
        ans = 0
        if d > m:
            ans = 


square()