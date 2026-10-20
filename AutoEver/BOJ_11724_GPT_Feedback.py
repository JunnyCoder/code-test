N, M = map(int, input().split())

arr = [[] for _ in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

nodes = set(range(1, N + 1))
chunks = 0

while nodes:
    s = nodes.pop()
    chunks += 1

    stack = [s]

    while stack:
        node = stack.pop()

        for nxt in arr[node]:
            if nxt in nodes:
                nodes.remove(nxt)
                stack.append(nxt)

print(chunks)