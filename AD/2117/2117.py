import sys
sys.stdin = open("input.txt", "r")

T = int(input())

dr = [-1,1,0,0]
dc = [0,0,-1,1]


def calc_cost(k):
    return k ** 2 + (k - 1) ** 2

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    house_cnt = 0
    arr = []
    for i in range(N) :
        arr.append(list(map(int, input().split())))
        house_cnt += sum(arr[i])
    protected_houses = 0
    if house_cnt * M >= calc_cost(2 * N - 1): # 전영역을 커버하더라도 비용이 남으므로 계산 필요없음
        protected_houses = house_cnt
        print("all")
    else :
        # K를 하나 늘리는게 가치가 있는지 확인하는 함수
        # 만일 K를 하나를 늘렸을 때의 공간에 모든 집이 다 있을 때를 가정하고 그 비용이 양수 혹은 0 이면 참
        def is_valuable(k, house_left_cnt):
            return calc_cost(k + 1) - calc_cost(k) <= house_left_cnt * M

        def get_house (r, c, k) :
            h_cnt = 0
            k=k-1
            for nr in range(max(0, r - k), min(N, r + k + 1)):
                remain = k - abs(nr - r)
                for nc in range(max(0, c - remain), min(N, c + remain + 1)):
                    h_cnt += arr[nr][nc]
            return h_cnt



        for r in range(N):
            for c in range(N) :
                protected_house_cnt = arr[r][c]
                k = 1
                house_left_cnt = house_cnt - protected_house_cnt
                cost = M * protected_house_cnt - 1

                while k < 2 * N +1:
                    k += 1
                    temp = get_house(r, c, k)
                    house_left_cnt = house_cnt - temp
                    new_cost = temp * M - calc_cost(k)
                    if new_cost >= 0:
                        protected_house_cnt = temp
                protected_houses= max(protected_houses, protected_house_cnt)


    print(f"#{test_case} {protected_houses}")
