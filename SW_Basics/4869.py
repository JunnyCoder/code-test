# 4869. [S/W 문제해결 기본] 4일차 - 종이붙이기
memo = [-1..,1,2,3,3,12,]
def dp(N) :
    if memo[N] != -1 :
        return memo[N]
    if N == 1 :
        return 1
    if N == 2 :
        return 3

    return dp(N-1) + 2 * dp(N-2)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    print(f"#{test_case} {dp(N )}")