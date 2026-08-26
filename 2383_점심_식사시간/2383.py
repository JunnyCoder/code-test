"""

이동 완료 시간은 모든 사람들이 계단을 내려가 아래 층으로 이동을 완료한 시간이다.

사람들이 아래층으로 이동하는 시간은 계단 입구까지 이동 시간과 계단을 내려가는 시간이 포함된다.


    ① 계단 입구까지 이동 시간
        - 사람이 현재 위치에서 계단의 입구까지 이동하는데 걸리는 시간으로 다음과 같이 계산한다.
        - 이동 시간(분) = | PR - SR | + | PC - SC |
          (PR, PC : 사람 P의 세로위치, 가로위치, SR, SC : 계단 입구 S의 세로위치, 가로위치)

    ② 계단을 내려가는 시간
        - 계단을 내려가는 시간은 계단 입구에 도착한 후부터 계단을 완전히 내려갈 때까지의 시간이다.
        - 계단 입구에 도착하면, 1분 후 아래칸으로 내려 갈 수 있다.
        - 계단 위에는 동시에 최대 3명까지만 올라가 있을 수 있다.
        - 이미 계단을 3명이 내려가고 있는 경우, 그 중 한 명이 계단을 완전히 내려갈 때까지 계단 입구에서 대기해야 한다.
        - 계단마다 길이 K가 주어지며, 계단에 올라간 후 완전히 내려가는데 K 분이 걸린다.


사람의 위치와 계단 입구의 위치 및 계단의 길이 정보가 표시된 N*N 크기의 지도가 주어진다.

이때, 모든 사람들이 계단을 내려가 이동이 완료되는 시간이 최소가 되는 경우를 찾고,

그 때의 소요시간을 출력하는 프로그램을 작성하라.




[예시]

방의 한 변의 길이 N 이 5인 지도가 [Fig. 2]와 같이 주어진 경우를 생각해보자.

지도 내에 1 은 사람을 나타내고, 2 이상 10 이하의 숫자는 계단의 입구를 나타내며 해당 숫자는 계단의 길이를 의미한다.

[Fig. 2]에는 사람 6명이 있고, 계단은 2개가 있으며 길이는 각각 3과 5이다.
"""
arr = [[0, 1, 1, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 5, 0, 0]]


import heapq

# T = int(input())
T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N = int(input())
    N = 5
    # arr = []
    # for _ in range(N):
    #     arr.append(list(map(int, input().split())))
    
    persons = []
    stairs = []
    for ir, r in enumerate(arr) :
        for ic, c in enumerate(r) :
            if c == 1 :
                persons.append((ir,ic))
            elif c > 1 :
                stairs.append( ((ir,ic) , c))


    dist_dict = {}
    
    stair_0_pos = stairs[0][0]
    stair_1_pos = stairs[1][0]
    
    stair_0_len = stairs[0][1]
    stair_1_len = stairs[1][1]

    # 1. 각 계단과 사람의 거리 구하기
    for person in persons :
        dist_0 = abs(stair_0_pos[0] - person[0]) + abs(stair_0_pos[1] - person[1])
        dist_1 = abs(stair_1_pos[0] - person[0]) + abs(stair_1_pos[1] - person[1])

        dist_dict[person] = (dist_0, dist_1)

    elapsed_time = 999_999
    for mask in range(1 << len(persons)):
        dist_heap = [[], []] # heap으로 사용할 것

        for i in range(len(persons)):
            idx = (bool(mask & (1 << i)) * 1)
            heapq.heappush(dist_heap[idx], dist_dict[persons[i]][idx] )
        in_0 = []
        in_1 = []

        while dist_heap[0] :
            prior_3 = in_0[max(0, len(in_0)-3) : len(in_0)]
            if len(prior_3) == 3 :
                in_time = max(heapq.heappop(dist_heap[0]) + 1, prior_3[0] + stair_0_len )
                in_0.append(in_time)
            else :
                in_0.append(heapq.heappop(dist_heap[0]) + 1)

        while dist_heap[1] :
            prior_3 = in_1[max(0, len(in_1)-3) : len(in_1)]
            if len(prior_3) == 3 :
                in_time = max(heapq.heappop(dist_heap[1]) + 1, prior_3[0] + stair_1_len  )
                in_1.append(in_time)
            else :
                in_1.append(heapq.heappop(dist_heap[1]) + 1)
        if not in_0 :
            in_0.append(-stair_0_len)
        if not in_1 :
            in_1.append(-stair_1_len)

        elapsed_time = min(elapsed_time, max(max(in_0) + stair_0_len, max(in_1) + stair_1_len))

    print(f"#{test_case} {elapsed_time}")