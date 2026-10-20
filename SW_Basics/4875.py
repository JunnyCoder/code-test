T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    maze = []

    for i in range(N) :
        maze.append(list(map(int,input())))
        if 2 in maze[i] :
            start_row = i
            start_col = maze[i].index(2)
        if 3 in maze[i] :
            goal_row = i
            goal_col = maze[i].index(3)

    curr = (start_row, start_col)
    visited = [[False]*N for i in range(N)]


    def delta(r, c):
        res = []
        if 0 < r and not visited[r-1][c] and maze[r-1][c] != 1:
            res.append((r - 1, c))  # 상
        if r < N -1 and not visited[r+1][c] and maze[r+1][c] != 1:
            res.append((r + 1, c))  # 하
        if 0 < c and not visited[r][c-1] and maze[r][c-1] != 1:
            res.append((r, c - 1))  # 좌
        if c < N - 1 and not visited[r][c+1] and maze[r][c+1] != 1:
            res.append((r, c + 1))  # 우
        return res


    visited[curr[0]][curr[1]] = True
    d = delta(*curr)
    while d :
        curr = d.pop()
        r = curr[0]
        c = curr[1]
        visited[r][c] = True
        if maze[r][c] == 3 :
            print(f"#{test_case} 1")
            break
        d.extend(delta(*curr))
    else:
        print(f"#{test_case} 0")