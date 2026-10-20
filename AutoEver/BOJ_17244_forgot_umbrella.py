# from itertools import permutations, accumulate
from functools import lru_cache
from collections import deque


dr = [-1,1,0,0]
dc = [0,0,-1,1]

M, N = map(int, input().split())

arr = []

targets = []

for i in range(N):
    temp = list(input())
    arr.append(temp)
    for j, v in enumerate(temp):
        if v == "S":
            S = (i, j)
        elif v == "X":
            targets.append((i, j))
        if v == "E":
            E = (i, j)

# 간선간 거리 2차원 배열로 만들기

# 순서를 따져야 하는가? yes, 거리가 달라짐 => 비트마스크 bfs

target_cnt = len(targets)

@lru_cache
def bfs(start, end):
    dq = deque([(*start, 0)])
    visited = {start}
    while dq :
        r, c, d = dq.popleft()
        if (r, c) == end:
            return d

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] != '#' and (nr, nc) not in visited :
                dq.append((nr, nc, d+1))
                visited.add((nr,nc))



dist = [[float('inf')] * target_cnt for _ in range(1<<target_cnt) ]

for i, v in enumerate(targets):
    dist[1<<i][i] = bfs(S,v)

for i in range(1<<target_cnt) :
    for j in range(target_cnt):
        if dist[i][j] != float('inf'):
            for k in range(target_cnt):
                if not (i>>k) & 1 :
                    mask = i + (1<<k)
                    # dist[mask][k] = dist[i][j] +  bfs(targets[j],targets[k])
                    # 덮어씌워지는 케이스를 없애기 위해
                    dist[mask][k] = min(
                        dist[mask][k],
                        dist[i][j] + bfs(targets[j], targets[k]))

print(min([bfs(targets[i],E) + d for i, d in enumerate(dist[-1])]))






# candidates = []
# for i in permutations(targets, len(targets)) :
#     r, c = zip(*i)
#     a = map(lambda x : abs(x[0]-x[1]),  zip([sr, *r], [*r, E[0]]))
#     b = map(lambda x : abs(x[0]-x[1]),  zip([sc, *c], [*c, E[1]]))
#     candidates.append(sum(a) + sum(b))

# print(min(candidates))
