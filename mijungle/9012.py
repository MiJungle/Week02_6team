import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

T = int(input())
M = [input().rstrip() for _ in range(T)]

for i in M:
    leftcount = 0
    rightcount = 0
    for j in range(len(i)):
        if i[j] == "(":
            leftcount+= 1
        if i[j] ==")":
            rightcount+= 1
    if leftcount != rightcount:
        print("NO")
    else:
        print("YES")