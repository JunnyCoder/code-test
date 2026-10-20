# 1215. [S/W 문제해결 기본] 3일차 - 회문1
import sys
sys.stdin = open("1215.txt", "r")

T = 10

for test_case in range(1, T + 1):
    n = int(input())
    arr = [input() for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8-n+1):
            horizontal = arr[i][j:j+n]
            if horizontal == horizontal[::-1]:
                cnt += 1
            temp = list(zip(*arr))[i]
            # print(temp)
            vertical = ''.join(temp[j:j+n])
            # print(vertical)

            if vertical == vertical[::-1]:
                cnt += 1
    print(f"#{test_case} {cnt}")



