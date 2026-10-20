from collections import deque
T = 10

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


for test_case in range(1, T + 1):
    _ = input()
    N = 16
    house_cnt = 0
    arr = []
    dist = [[-1] * N for _ in range(N) ]
    for i in range(N) :
        arr.append(list(map(int, input())))
        if 3 in arr[i] :
            goal = (i, arr[i].index(3))
        if 2 in arr[i] :
            start = (i, arr[i].index(2))

    r, c = start
    dq = deque([start])
    d = 0
    dist[r][c] = 0
    res = 0
    while dq :
        r, c = dq.popleft()
        d = dist[r][c]
        if (r, c) == goal :
            res = 1
            break
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < N and 0<=nc<N and arr[nr][nc] != 1 and dist[nr][nc] == -1 :
                dist[nr][nc] = d + 1
                dq.append((nr, nc))

    print(f"#{test_case} {res}")