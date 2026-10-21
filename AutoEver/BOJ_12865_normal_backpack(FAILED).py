N, K = map(int, input().split())

arr = [(0,0)]
dp = [[0] * (K + 1) for _ in range(N + 1)]
# overK = set() # w 자체가 k를 넘어서 아예 담을 수 없는 물건의 인덱스
for i in range(N):
    w, v = map(int, input().split())
    if K >= w :
        # dp[1][w] = v
        arr.append((w,v))           
    # if w > K:
    #     overK.add(i)

# memo = [[0] * N for _ in range(K + 1)]
# maxV = [0] * (K+1)
# for i, (w, v) in enumerate(arr) :
#     memo[w][i] = v


# max_val = 0

for i in range(1, N+1):
    for k in range(1, K+1):
        if arr[i][0] <= k :
            w = arr[i][0]
            dp[i][k] = max(dp[i-1][k-w] + arr[i][1], dp[i-1][k])

print(max([dp[i][-1] for i in range(N+1)]))        

for i in dp:
    print(i)
        







# # 완탐 + 가지치기(1. K 넘어가는 순간  2. w가 K 넘어가는 인덱스 스킵)
# for i in range(1,1<<N):
#     val = 0
#     weight = 0
#     for j in range(N):
#         if (i >> j) & 1 :
#             if j in overK :
#                 break
#             weight += arr[j][0]

#             if weight > K :
#                 break

#             val += arr[j][1]

#     else :
#         if max_val < val :
#             max_val = val


# print(max_val)


# '''
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12
# '''