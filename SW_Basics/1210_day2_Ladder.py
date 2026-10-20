
# 1210. [S/W 문제해결 기본] 2일차 - Ladder1

import sys
sys.stdin = open("input_0903.txt", "r")

T = 10

for test_case in range(1, T + 1):
    _ = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    j = arr[-1].index(2)
    for i in range(99, -1, -1):
        if 0 < j:
            left = arr[i][j - 1]
        else:
            left = 0

        if j < 99:
            right = arr[i][j + 1]
        else:
            right = 0

        while left:
            if 0 < j:
                j -= 1
                left = arr[i][j - 1]
            else:
                left = 0

        while right:
            if j < 99:
                j += 1
                right = arr[i][j + 1] if j != 99 else 0
            else:
                right = 0
    print(f"#{test_case} {j}")