import sys

sys.stdin = open("4130.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    K = int(input())
    arr = []
    for i in range(4) :
        arr.append(list(map(int, input().split())))


    def turn_magnet(mag_num, dir, impact_on = 'LR'):
        # arr[mag_num - 1] 이 본인, [2] 가 오른쪽 [-2]가 왼쪽
        left = arr[mag_num-1][-2]
        right = arr[mag_num-1][2]
        # 오른쪽 돌리기
        if mag_num < 4 and "R" in impact_on:
            if right != arr[mag_num][-2] :
                turn_magnet(mag_num+1, -dir, "R")
        # 왼쪽 돌리기
        if mag_num > 1 and "L" in impact_on:
            if left != arr[mag_num-2][2] :
                turn_magnet(mag_num-1, -dir, "L")
        # 회전 결과 반영
        if dir == 1:
            arr[mag_num - 1] = [arr[mag_num - 1][-1]] + arr[mag_num - 1][:-1]
        else:
            arr[mag_num - 1] = arr[mag_num - 1][1:] + [arr[mag_num - 1][0]]


    for _ in range(K) :
        mag_num, dir = map(int, input().split())
        turn_magnet(mag_num, dir)

    score = arr[0][0] * 1 + arr[1][0] * 2 + arr[2][0] * 4 + arr[3][0] * 8
    print(f"#{test_case} {score}")