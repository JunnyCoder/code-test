# 4880. [S/W 문제해결 기본] 5일차 - 토너먼트 카드게임

def game(a, b) :
    return a if a[1]==b[1] or ((a[1], b[1]) in ((1,3), (2,1), (3,2) )) else b

def Tournament(arr) :
    a_len = len(arr)
    if a_len == 1:
        return arr[0]
    if a_len == 2:
        return game(arr[0], arr[1])
    g1 = arr[:(a_len+1)//2]
    g2 = arr[(a_len+1) // 2:]
    return game(Tournament(g1), Tournament(g2))

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f"#{test_case} {Tournament(list(enumerate(arr, 1)))[0]}")

