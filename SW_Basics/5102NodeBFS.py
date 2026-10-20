from collections import deque, defaultdict
T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    dists = [-1] * (V+1)
    nodes = defaultdict(list)
    for i in range(E):
        n1, n2 = map(int, input().split())
        nodes[n1].append(n2)
        nodes[n2].append(n1)
    S, G = map(int, input().split())

    dists[S] = 0
    dq = deque([S])

    while dq :
        n = dq.popleft()
        d = dists[n]
        if n == G :
            break
        for i in nodes[n] :
            if dists[i] == -1:
                dists[i] = d + 1
                dq.append(i)
    if dists[G] == -1:
        print(f"#{test_case} 0")
    else :
        print(f"#{test_case} {dists[G]}")