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

from collections import defaultdict, deque


5




T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = 5 
    arr = [[0, 1, 1, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 5, 0, 0]]
    persons = []
    stairs = []
    dist_dict_0 = defaultdict(list) # key 
    dist_dict_1 = defaultdict(list) # key 

    # for _ in range(N):
    #     arr.append(list(map(int, input().split())))

    for ir, r in enumerate(arr) :
        for ic, c in enumerate(r) :
            if c == 1 :
                persons.append((ir,ic,))
            elif c > 1 :
                stairs.append( ((ir,ic,) , c,))

    stair_0_pos = stairs[0][0]
    stair_1_pos = stairs[1][0]
    
    stair_0_len = stairs[0][1]
    stair_1_len = stairs[1][1]

    for person in persons :
        dist_0 = abs(stair_0_pos[0] - person[0]) + abs(stair_0_pos[1] - person[1])
        dist_1 = abs(stair_1_pos[0] - person[0]) + abs(stair_1_pos[1] - person[1])

        dist_dict_0[dist_0].append(person)
        dist_dict_1[dist_1].append(person)

    elapsed_time = 0
    curr_time = 9999999
    in_0 = deque()
    in_1 = deque()
    stair_0 = 0
    stair_1 = 0
    print(f"curr{curr_time}, elap {elapsed_time}, ramain{persons}")
    while persons :
        if stair_0 == 0 :
            min_key_0 = min(dist_dict_0.keys())
            stair_0 = dist_dict_0[min_key_0].pop()
            print(0)
            if not dist_dict_0[min_key_0] :
                del dist_dict_0[min_key_0]

        if stair_1 == 0 :
            min_key_1 = min(dist_dict_1.keys())
            stair_1 = dist_dict_1[min_key_1].pop()
            print(1)

            if not dist_dict_1[min_key_1] :
                del dist_dict_1[min_key_1]

        expected_out_0 = min_key_0 + 1 + stair_0_len
        expected_out_1 = min_key_1 + 1 + stair_1_len

        if expected_out_0 < expected_out_1 :
            in_0.append((expected_out_0, stair_0, ))
            temp_time = min_key_0
            print("out:",stair_0, "to 0")
            persons.remove(stair_0)
            stair_0 = 0
            for i in in_0 :
                if i[0] <= elapsed_time :
                    in_0.popleft()
                else :
                    break

        else :
            in_1.append((expected_out_1, stair_1, ))
            temp_time = min_key_1
            print("out:",stair_1, "to 1")

            persons.remove(stair_1)
            stair_1 = 0

            for i in in_1 :
                if i[0] <= elapsed_time :
                    in_1.popleft()
                else :
                    break

        if temp_time > curr_time :
            elapsed_time = curr_time + 1

        curr_time = temp_time

        print(f"curr{curr_time}, elap {elapsed_time}, ramain{persons}")


        

    # latest_arrival_0 = max(dist_dict_0.keys())
    # latest_arrival_1 = max(dist_dict_1.keys())

    # if stair_0_len < stair_1_len:
    #     in_active_stair = [].extend(v for j, v in dist_dict_0.items() if latest_arrival_0 - j > stair_0_len )
    # else :
    #     in_active_stair = [].extend(v for j, v in dist_dict_1.items() if latest_arrival_1 - j > stair_1_len )

    # s







    

'''
거리를 계산하고 
왼쪽 오른쪽 계단을 여기서 바로 배정을 해보자.

'''







    # # is_0_short = stair_0_len <= stair_1_len
    
    # in_time_0 = deque()
    # in_time_1 = deque()


    # for v in persons :
    #     for stair in stairs :
    #         dist_dict[stair].append(tuple(abs(v[0] - stair[0][0]) + abs(v[1] - stair[0][1]), v) )


    # for k in dist_dict :
    #     dist_dict[k].sort(reverse=True)

    # elapsed_time = 0
    # maxtime = 

    # while len(persons) > 0 :
    #     stair_0 = dist_dict[0].pop()
    #     stair_1 = dist_dict[1].pop()

    #     if  stair_0[1] + stair_0_len < stair_1[1] + stair_1_len :
    #         while stair_0[1] + stair_0_len < stair_1[1] + stair_1_len :
    #             in_time_0.append(stair_0[1] + 1 + stair_0_len)




    #         stair_0 = dist_dict[0].pop()




    #     persons.remove(position)
