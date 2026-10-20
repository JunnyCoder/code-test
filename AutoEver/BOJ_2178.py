from collections import deque
N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
dist = [[0] * M for _ in range(N)]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

dq = deque([(0, 0)])
dist[0][0] = 1

while dq :
    r, c = dq.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<= nr < N and 0<= nc < M :
            if arr[nr][nc] and not dist[nr][nc] :
                dq.append((nr,nc))
                dist[nr][nc] = dist[r][c] + 1
    if dist[N-1][M-1] :
        break

print(dist[N-1][M-1])