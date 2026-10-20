#4881. [S/W 문제해결 기본] 5일차 - 배열 최소 합
from itertools import permutations

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # min_sum = min(map(sum, map(lambda x : [arr[i][x[i]] for i in range(N)], permutations([i for i in range(N)], N))))

    used = [False] * N
    min_sum = N * 9

    def dfs(row, total):
        global min_sum

        if total >= min_sum:
            return

        if row == N:
            min_sum = total
            return

        for col in range(N):
            if not used[col]:
                used[col] = True
                dfs(row + 1, total + arr[row][col])
                used[col] = False


    dfs(0, 0)

    print(f"#{test_case} {min_sum}")

