# https://claude-u.tistory.com/448
# https://tmdrl5779.tistory.com/119


import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

x, y = map(int, input().split())
house = [int(input().rstrip()) for _ in range (x)]
house.sort()

def binary():
    left = 1
    right = max(house) - 1

    while left <= right:
        mid = (left + right) // 2
        count = 1
        wifi = min(house) + mid

        for i in range(1, len(house)):
            if wifi <= house[i]:
                count += 1
                wifi = house[i] + mid

        if count >= y:
            left = mid + 1
        elif count < y:
            right = mid - 1
    return right
print(binary())
