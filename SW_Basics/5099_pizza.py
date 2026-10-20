from collections import deque
T = int(input())

def get_time(n):
    k = 0
    while n > 0 :
        k+=1
        n //= 2
    return k


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    cheez = list(map(int, input().split()))
    times = list(map(get_time, cheez))
    in_oven = times[:N]
    in_oven_idx = [i for i in range(1, N+1)]
    wait = deque(times[N:])
    wait_head_idx = N+1
    while wait :
        next_out_time = min(in_oven)
        in_oven = list(map(lambda x : x - next_out_time, in_oven))
        for i, v in enumerate(in_oven):
            if v == 0 and wait:
                in_oven[i] = wait.popleft()
                in_oven_idx[i] = wait_head_idx
                wait_head_idx += 1

    a = list()
    a.insert()
    print(f"#{test_case} {in_oven_idx[N - in_oven[::-1].index(max(in_oven)) - 1]}")




# 3 1 3 2 1
# 1 0 1 1 0
# 0 0 0 0 0






