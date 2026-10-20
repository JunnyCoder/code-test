from collections import deque
T = 10
for test_case in range(1, T + 1):
    _ = input()
    arr = list(map(int,input().split()))
    dq = deque(arr)
    cycle = [i for i in range(1, 6)]
    i = 0
    while dq[-1] :
        a = dq.popleft()
        a = max(0, a - cycle[i])
        i = (i + 1) % 5
        dq.append(a)

    print(f"#{test_case} {' '.join(map(str, dq))}")