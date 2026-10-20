from collections import defaultdict

def dfs(start,goal,visited):
    visited[start] = True
    if goal in graph[start]:
        return True

    for node in graph[start]:
        if not visited[node]:
            if dfs(node, goal, visited) :
                return True
    return False



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    visited = [False] * (V+1)
    for i in range(E) :
        start, end = map(int, input().split())
        graph[start].append(end)
    S, G = map(int, input().split())
    print(f"#{test_case} {int(dfs(S, G, visited))}")
