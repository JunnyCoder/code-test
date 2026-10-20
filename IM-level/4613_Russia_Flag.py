# 4613. 러시아 국기 같은 깃발
import sys
sys.stdin = open("4613_input.txt", "r")

# 누적합
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    color_order = 'WBR'
    color_cnt_cum_arr = [] # 어차피 순회해야함으로 누적합으로 구하기
    color_cnt_cum_arr.append([0, 0, 0]) # 1열은 흰색 고정임으로 무시하기./

    for i, colors in enumerate(arr[1:-1], 1):
        color_cnt_cum_arr.append([M - colors.count(color) + color_cnt_cum_arr[i - 1][j] for j, color in enumerate(color_order)])
    mid_rows_cnt = len(color_cnt_cum_arr) - 1
    color_cnt_cum_arr.append(color_cnt_cum_arr[-1])  # 마지막열은 빨간색 고정임으로 무시하기./
    cost = 50 * 50
    for i in range(mid_rows_cnt):
        for j in range(mid_rows_cnt - i):
            new_cost_w = color_cnt_cum_arr[i][0]
            new_cost_b = color_cnt_cum_arr[mid_rows_cnt-j][1] - color_cnt_cum_arr[i][1]
            new_cost_r = color_cnt_cum_arr[mid_rows_cnt][2] - color_cnt_cum_arr[mid_rows_cnt-j][2]
            new_cost = new_cost_w + new_cost_b + new_cost_r
            cost = min(cost, new_cost)
    print(f"#{test_case} {cost + 2* M - arr[0].count('W') - arr[-1].count('R')}")

# 최초풀이
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [input() for _ in range(N)]
#     color_order = ['W', "B", "R"] ## 굳이 리스트로 안하고 문자열로 해도됨
#     color_cnt_arr = []
#     for colors in arr:
#         ## M 에서 뺀 값을 저장해놓으면 굳이 뒤에서 람다 쓸 필요 없어짐
#         # color_cnt_arr.append([M - colors.count(color) for color in color_order])
#         color_cnt_arr.append([colors.count(color) for color in color_order])
#     min_cnt = sum(color_cnt_arr[0][1:]) + sum(color_cnt_arr[-1][:2]) # 첫줄, 마지막 줄 기본 색칠 값
#     mid_rows_cnt = len(color_cnt_arr[1:-1])
#     mid_cnt = 50 * 50 # 최대 색칠개수 범위 가정
#     for i in range(mid_rows_cnt):
#         for j in range(mid_rows_cnt - i):
#             cnt_w = sum(map(lambda x : x[1] + x[2], color_cnt_arr[1:i+1]))
#             cnt_b = sum(map(lambda x : x[0] + x[2], color_cnt_arr[i+1:mid_rows_cnt-j+1]))
#             cnt_r = sum(map(lambda x : x[0] + x[1], color_cnt_arr[mid_rows_cnt-j+1:-1]))
#             mid_cnt = min(mid_cnt, cnt_w + cnt_b + cnt_r)
#
#     print(f"#{test_case} {min_cnt + mid_cnt}")