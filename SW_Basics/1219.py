from collections import defaultdict, deque

T = 10

for test_case in range(1, T + 1):
    _, N = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(N*2, step=2) :
        graph[arr[i]].append(arr[i+1])

    visited = [False] * 100 # 0 ~ 99
    visited[0] = True

    start = 0
    dq = deque(graph[start])
    res = 0
    while dq :
        destination = dq.popleft()
        if destination == 99 :
            res = 1
            break
        if not visited[destination] :
            dq.extend(graph[destination])
    print(f"#{test_case} {res}")