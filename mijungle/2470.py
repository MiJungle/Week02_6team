import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split()))
M.sort()

def closetozero():
    first = 0
    end = len(M) - 1
    count = []
    while first <= end:
        mid = (first + end)//2
        for i in M:
            k = abs(i + M[mid])
            if i != M[mid]:
                count.append([k, i, M[mid]])
                first = mid +1 
    print(count)
    for i in count:
        if i[0] == 0:
            ans = i[1:]
            print(*ans, sep = ' ')
            break
        else:
            ans = min(count)[1:]
            print(*ans, sep = ' ')
            break

closetozero()