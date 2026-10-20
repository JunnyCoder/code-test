from collections import defaultdict
T = int(input())

for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    edges = defaultdict(list)
    for i in range(E):
        edges[arr[2*i]].append(arr[2*i+1])
    keys = [N]
    childs = 0
    while keys :
        n = keys.pop()
        childs +=1
        print(edges, n)
        if n in edges.keys() :
            keys.extend(edges[n])
    print(f"#{test_case} {childs}")