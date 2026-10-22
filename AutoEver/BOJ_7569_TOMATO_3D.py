from collections import deque

N, M, H = map(int, input().split())

arr = []
dist = [[float('inf')] * N for _ in range(M * H)]
tomatos = deque([])
empty =set()
for i in range(M * H):
    temp = list(map(int, input().split()))
    arr.append(temp)
    for j, v in enumerate(temp):
        if v == 1 :
            tomatos.append((i, j))
            dist[i][j] = 0
        if v == -1 :
            empty.add((i,j))
            dist[i][j] = 0
res = 0
if len(tomatos) + len(empty) != N * M * H :
    # 상 하 좌 우 ] [차원이동 상 하]
    dr = [-1, 1, 0, 0, 0, 0]
    dc = [0, 0, -1, 1, 0, 0]
    dz = [0,0,0,0,1,-1]


    while tomatos :
        r, c = tomatos.popleft()
        edge = r % M  # 0 이면 상 금지, M-1 이면 하 금지
        for i in range(6):
            if (edge == 0 and i == 0 ) or  (edge == M-1 and i == 1 ):
                continue
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < M * H and 0<= nc < N :
                if not arr[nr][nc] and dist[nr][nc] == float('inf') :
                    tomatos.append((nr,nc))
                    dist[nr][nc] = dist[r][c] + 1

    res = max(map(max, dist))
    if res == float('inf') :
        res = -1
print(res)