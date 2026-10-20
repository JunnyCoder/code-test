import sys
sys.stdin = open("input_1209.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    _ = int(input())
    arr = []
    ver_sum = [0] * 100
    hor_sum = [0] * 100

    cross_sum = [0, 0]
    for i in range(100):
        temp = list(map(int, input().split()))

        for j, v in enumerate(temp):
            ver_sum[j] += v
            hor_sum[i] += v
            if i == j:
                cross_sum[0] += v
            elif i == 99 - j:
                cross_sum[1] += v

    print(f"#{test_case} {max(max(ver_sum), max(hor_sum), max(cross_sum))}")


outer_list = [[i + 10 * j for i in range(1, 11)] for j in range(10)]

for inner_list in outer_list :
    for elements in inner_list :
        print(elements, end=" ")


for i in range(10) :
    for j in range(10) :
        print(outer_list[i][j], end=" ")
    print()