from collections import defaultdict 
import heapq

N = int(input())
M = int(input())

graph = defaultdict(list)

dist = [float('inf')] * (N+1)

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((c, e))

S, E = map(int, input().split())

# 다익스트라 위한 출발지 초기화
hq =[(0, S)]
heapq.heapify(hq)

while hq:
    c_cost, cur = heapq.heappop(hq)

    # 비효율 재방문 방지
    if dist[cur] <= c_cost:
        continue

    dist[cur] = c_cost

    # 다익스트라 이므로 최초방문(꺼낼때) => 최적해 보장
    if cur == E:
        break

    for (n_cost, next) in graph[cur]:
        if dist[next] > c_cost + n_cost :
            heapq.heappush(hq,(c_cost + n_cost, next))
                

print(dist[E])