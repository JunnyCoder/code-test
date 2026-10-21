N, K = map(int, input().split())

arr = [(0,0)]
dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(N):
    w, v = map(int, input().split())
    arr.append((w,v))           

for i in range(1, N+1):
    for k in range(1, K+1):
        if arr[i][0] <= k :
            w = arr[i][0]
            dp[i][k] = max(dp[i-1][k-w] + arr[i][1], dp[i-1][k])
        else :
            dp[i][k] = dp[i-1][k]

print(dp[N][K])        

# for i in dp:
#     print(i)
        

