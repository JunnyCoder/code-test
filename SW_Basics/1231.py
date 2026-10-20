from collections import defaultdict
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    edges = defaultdict(dict)
    nodes = [""] * (N+1)

    for i in range(N):
        temp = list(input().split())
        nodes[int(temp[0])] = temp[1]
        if len(temp) > 2:
            edges[int(temp[0])]["L"] = int(temp[2])
        if len(temp) == 4:
            edges[int(temp[0])]["R"] = int(temp[3])

    def get_order(start) :
        if start not in edges :
            return [start]
        if "R" in edges[start] :
            return get_order(edges[start]["L"]) + [start] + get_order(edges[start]["R"])
        else:
            return get_order(edges[start]["L"]) + [start]
    print(f"#{test_case} ", end="")
    for i in get_order(1):
        print(nodes[i], end="")
    print()