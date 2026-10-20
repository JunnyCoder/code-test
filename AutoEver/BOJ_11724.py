N, M = map(int, input().split())

arr = [list() for _ in range(N + 1)]

# 모든 정점이 간선을 가진다는 보장이 없으므로 dfs/bfs 시 출발점 set에서 팝
nodes = set(i for i in range(1, N+1))
chunks = N
for _ in range(M):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

while nodes :
    s = nodes.pop()
    # DFS 시작
    connected = arr[s].copy()
    while connected :
        e = connected.pop()
        if e in nodes:
            nodes.remove(e)
            chunks -= 1 
            connected.extend(arr[e])

print(chunks)