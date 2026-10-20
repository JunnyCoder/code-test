T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    edges_parents = [ i // 2 for i in range(N + 1)]
    edges_children = [0] + [[i*2,  i*2+1] for i in range(1,(N+1)//2)] +[0] * (N - (N+1)//2 )
    node_vals = [0] * (N+1)
    last_node = 1
    node_vals[last_node] = arr[0]
    for i in arr[1:]:
        new_node = last_node + 1
        node_vals[new_node] = i
        curr_node = new_node
        p = edges_parents[curr_node]
        while node_vals[new_node] < node_vals[p] :
            while p > 0 :
                if node_vals[curr_node] < node_vals[p] :
                    node_vals[curr_node], node_vals[p] = node_vals[p], node_vals[curr_node]
                curr_node = p
                p = edges_parents[curr_node]
        last_node += 1

    parents = []
    while N > 0:
        parents.append(edges_parents[N])
        N //= 2
    print(f"#{test_case} {sum(map(lambda x : node_vals[x], parents))}")