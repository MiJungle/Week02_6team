# 소스: https://claude-u.tistory.com/446
# Pypy로만 됨

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
Tree = list(map(int, input().split()))
Tree.sort()
start, end = 1, max(Tree)

while start <= end:
    mid = (start+end) //2

    log = 0
    for i in Tree:
        if i >= mid:
            log += i - mid
            
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)