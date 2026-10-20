from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(M)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#벽 안뿌순거
dist = [[float('inf')] * N for _ in range(M)]
# 벽 뿌순순간
dist_k = [[float('inf')] * N for _ in range(M)]
dist[0][0] = 1
#(r, c, 잔여 벽 뿌수기 찬스)
dq = deque([(0, 0, 1)])


while dq :
    r, c, k = dq.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<= nr < M and 0 <= nc < N :
            if k :
                if dist[nr][nc] == float('inf'):
                    # 벽이 아닐 때
                    if arr[nr][nc] == 0:
                        dist[nr][nc] = dist[r][c] + 1
                        dq.append((nr, nc, k))

                    # 최초로 벽을 만나서 깰 때, k 위에서 검증했으니 검증 필요없음.
                    elif dist_k[nr][nc] == float('inf') and arr[nr][nc] == 1 :
                        dist_k[nr][nc] = dist[r][c] + 1
                        dq.append((nr, nc, 0))

            # 기회를 소진하고 나아갈 때
            elif dist_k[nr][nc] == float('inf'): 
                if arr[nr][nc] == 0:
                    dist_k[nr][nc] = dist_k[r][c] + 1
                    dq.append((nr, nc, 0))

if dist[-1][-1] != float('inf') or  dist_k[-1][-1] != float('inf'):
    res = min( dist[-1][-1] ,  dist_k[-1][-1])
else :
    res = -1

print(res)
