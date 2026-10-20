import sys

sys.stdin = open("5653.txt", "r")

f = open('test.txt', 'w')

from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

T = int(input())
for test_case in range(1, T + 1):
    wait = deque()
    active = deque()
    # dead = []
    # cells = lambda: wait + active + dead
    # alive = lambda: wait + active
    curr = 0
    N, M, K = map(int, input().split())
    K += 50
    # arr = [list(map(int,input().split())) for _ in range(N)]
    power = [[0] * (2 * K ) for _ in range(2 * K + 100)]
    status = [[0] * (2 * K ) for _ in range(2 * K + 100)]
    active_time = [[0] * (2 * K ) for _ in range(2 * K + 100)]
    # 0 empty, 1 wait, 2 active, 3 dead
    for r in range(N):
        temp = list(map(int, input().split()))
        for c in range(M):
            if temp[c]:
                power[K + r][K + c] = temp[c]
                status[K + r][K + c] = 1
                active_time[K + r][K + c] = curr + temp[c]
                wait.append((K + r, K + c)) # power, r, c
    K -= 50
    curr = 0
    while curr <= K :
        active_cnt = len(active) # 현재 시점에 들어온 애들만 하기 위해 최초에 카운트
        # 셀 깨우기
        for i in range(len(wait)):
            r, c = wait.popleft()
            if active_time[r][c] == curr :
                active.append((r, c))
                active_time[r][c] += power[r][c]
                status[r][c] = 2
            else :
                wait.append((r, c))
        # 증식
        for i in range(active_cnt) :
            r, c = active.popleft()
            p = power[r][c]
            is_first_active = active_time[r][c] - curr - p + 1 == 0
            if is_first_active :
                # 움직이기
                born = {} # 동시배양 때문에 보관해놨다가 배양해줘야함
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if  status[nr][nc] == 0: # 배열크기는 최대 K의 두배로 줬으니 범위 고려 X
                        if (nr, nc) not in born:
                            born[(nr, nc)] = p
                        else:
                            born[(nr, nc)] = max(born[(nr, nc)], p) # 동시 배양 고려

                for (nr, nc), p in born.items():
                    power[nr][nc] = p
                    active_time[nr][nc] = curr + p
                    status[nr][nc] = 1
                    wait.append((nr, nc))

            if active_time[r][c] == curr :
                status[r][c] = 3
            else :
                active.append((r, c))

        curr += 1
    print(f"#{test_case} {len(active)+ len(wait)}")
    print(test_case, file=f)
    print([i for i in range(2 * K )], file=f)
    for i,v in enumerate(active_time):
        print(i, v,  file=f)
f.close()
    # if test_case == 1 :
    #     print(wait,len(cells()),test_case)
    #     print("\n\n\n")