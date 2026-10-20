# 2115. [모의 SW 역량테스트] 벌꿀채취
import heapq
T = int(input())

for tc in range(1, T + 1) :
    N, M, C = map(int, input().split())

    sum_val = [ list() for _ in range(N)]
    
    for i in range(N) :
        temp = list(map(int, input().split()))
        max_val = 0
        for j in range(N-M) :
            cur_sum = sum(temp[j:j+M])
            sum_val[i].append((-cur_sum, j))
            if max_val < cur_sum :
                max_val = cur_sum

        heapq.heapify(sum_val[i])
    
    print(sum_val)

