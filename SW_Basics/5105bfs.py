from collections import deque
T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


for test_case in range(1, T + 1):
    N = int(input())
    house_cnt = 0
    arr = []
    dist = [[float("inf")] * N for _ in range(N) ]

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
    while dq :
        r, c = dq.popleft()
        d = dist[r][c]
        if (r, c) == goal :
            break
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < N and 0<=nc<N and arr[nr][nc] != 1 and dist[nr][nc] > d + 1 :
                dist[nr][nc] = d + 1
                dq.append((nr, nc))
    gr, gc = goal
    if dist[gr][gc] == float("inf"):
        print(f"#{test_case} 0")
    else:
        print(f"#{test_case} {dist[gr][gc]-1}")