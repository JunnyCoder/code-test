# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# grid = [
# [4, 2, 0, 8],
# [4, 2, 2, 4],
# [0, 8, 8, 2],
# [4, 2, 2, 2]
# ]

output_grid = [[], [], [], []]

# Read direction
dir = input()
# dir = "U"

dirs = "LRUD"
dc = [-1, 1, -1, 1]

# dirs.index(dir)
is_turned = False
if dir in "UD":
    grid = [x[::-1] for x in list(map(list, zip(*grid[::-1])))[::-1]] # 왼쪽 90도 회전
    is_turned = True


# 왼쪽 오른쪽용
for i, row in enumerate(grid):
    is_added = True
    for v in row[::-dc[dirs.index(dir)]]:
        if v == 0:
            continue
        if is_added:
            output_grid[i].append(v)
            is_added = False
        elif output_grid[i][-1] == v:
            output_grid[i][-1] += v
            is_added = True
        else:
            output_grid[i].append(v)

for i in range(4):
    if dir in "RD":
        output_grid[i] = (4 - len(output_grid[i])) * [0] + output_grid[i][:: -1]
    else:
        output_grid[i].extend((4 - len(output_grid[i])) * [0])

if is_turned :
    output_grid = list(map(list, zip(*output_grid[::-1])))


for i in output_grid :
    print(" ".join(map(str, i)))


grid = [
[4, 2, 0, 8],
[4, 2, 2, 4],
[0, 8, 8, 2],
[4, 2, 2, 2]
]

grid = [list(row) for row in zip(*grid)][::-1]