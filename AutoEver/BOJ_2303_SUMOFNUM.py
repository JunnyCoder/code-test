'''
문제 1. BOJ 2003 — 수들의 합 2
실버 4
문제 설명
N개의 자연수로 이루어진 수열이 주어진다.
이 수열에서 연속된 하나 이상의 원소를 선택하여 합이 M이 되는 경우의 수를 구하라.
선택하는 구간의 시작 위치나 끝 위치가 다르면 서로 다른 경우로 계산한다.
입력
첫째 줄에 N M이 주어진다.
둘째 줄에 N개의 자연수가 공백으로 구분되어 주어진다.
항목	제한
N	1 ≤ N ≤ 10,000
M	1 ≤ M ≤ 300,000,000
각 원소	1 이상 30,000 이하
출력
합이 M이 되는 연속 구간의 개수를 출력한다.
공식 예제 1 — 입력
4 2
1 1 1 1


출력
3


공식 예제 2 — 입력
10 5
1 2 3 4 2 5 3 1 1 2


출력
3

'''

MAX_INT = 30000

N, M = map(int, input().split())
arr = list(map(int, input().split()))


L = 0
R = 0
curval = arr[L]
cnt = 0
while L < N  :
    if curval < M  and R < N - 1:
        R += 1
        curval += arr[R]
    else :
        if curval == M :
            cnt += 1    
        curval -= arr[L]
        L += 1

print(cnt)



# 1차 시도 
# from collections import deque
# MAX_INT = 30000

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))


# L = 0
# R = 0
# curval = arr[L]
# cnt = 0
# while L < N - 1 :
#     if curval < M  and R < N - 1:
#         R += 1
#         curval += arr[R]
#     else :
#         if curval == M :
#             cnt += 1    
#         L += 1
#         R = L
#         curval = arr[L]

# print(cnt)
