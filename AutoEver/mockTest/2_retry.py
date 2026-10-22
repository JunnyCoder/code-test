import heapq

n, m = map(int, input().split())
# edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import deque

indgree = [0] * (n+1)
edges = [list() for _ in range(n+1)]

q = []

for _ in range(m) :
    x, y = map(int, input().split())
    edges[x].append(y)
    indgree[y] += 1

for i in range(1, n+1):
    if not indgree[i]:
        q.append(i)

while q :
    x = heapq.heappop(q)

    print(x, end=" ")

    for y in edges[x]:
        indgree[y] -= 1
        if not indgree[y]:
            heapq.heappush(q,y)



