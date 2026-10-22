from collections import deque
import heapq
# 1번 아이디어
# 연결된 리스트들의 청크를 구하고, 시작 노드가 가장 작은 것부터 배치, 
# 작은 청크의 뒷 원소가 뒷 청크의 앞쪽요소보다 크다면 그 뒤에 끼워넣기

# edge case 1 : 한 정점에 간선이 여러개
# edge case 2 : 실제 뒷 정점이 더 작을 때 ex) 2 4
# edge case 3 : 사이클이 있는 경우 => 2 와 같은말임, 취소

N, M = map(int,input().split())

graph = [ list() for _ in range(N+1)]


for _ in range(M) :
    s, e = map(int,input().split())
    if s > e : # edge case 2
        graph[e].append(s)
        # graph[s].append(e)

# 2번 아이디어
# 인덱스배열만들기
# idxs = [i for i in range(N+1)]

# for i in range(N,0,-1):
#     if graph[i] :
#         temp = sorted(graph[i])
#         idxs[i] = temp[0]
#         t_idx = idxs[i] +1
#         for idx in temp :
#             idxs[idx] = t_idx
#             t_idx += 1

# print(idxs)

sorted_arr = [0] * (N+1)

i = 1 
while i < N+1:
    if graph[i]:
        pass
    








# in_graph = set()
# chunks = []

# for _ in range(M):
#     s, e = map(int,input().split())
#     if s not in in_graph or e not in in_graph :
#         in_graph.add(s)
#         in_graph.add(e)



# in_graph = set()
# chunks = []
# # 청크구하기
# for i in range(1, N+1) :
#     if graph[i] :
#         chunk = deque([i])
#         dq = deque(sorted(graph[i]))
#         while dq :
#             s = dq.popleft()
#             in_graph.add(s)
#             chunk.appendleft(s)
#             if graph[s] :

#     in_graph.add(i)
# for _ in range(M) :



# # arr = deque([])
# arr = []
# visited = set()
# for i in range(1, N+1) :
#     if graph[i] :
#         dq = deque(sorted(graph[i]))
#         while dq
#     else: 
#         arr.append(i)


# 뒤에서 앞으로 연결된 간선의 최대값을 들고 
# for i in range(N,0,-1):


# for _ in range(M) :
#     s, e = map(int,input().split())
#     graph[e].append(s)
