from collections import deque
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    # temp =
    arr = list(map(int,input().split()))
    counting_p = [0] * (V+1)
    nodes = { i : list() for i in range(1, V+1)}

    for i in range(E):
        nodes[arr[2 * i]].append(arr[2 * i + 1])


    def parent_count(n) :
        if not nodes[n] :
            counting_p[n] = 1
            return 1
        li = []
        for i in nodes[n] :
            if counting_p[i] :
                li.append(parent_count(i))
            else :
                li.append(parent_count(i))
        return max(li) + 1

    for i in range(1, V+1) :
        counting_p[i] = parent_count(i)

    print("#"+str(test_case), " ".join(map(lambda x: str(x[0]), sorted(list(enumerate(counting_p[1:], 1)), key = lambda x : - x[1]))))
