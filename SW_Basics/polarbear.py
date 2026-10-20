#
#
# N, M = 5, 5
#
# arr = [
#     [0, 0, 0, 0, 0],
#     [0, 5, 4, 5, 0],
#     [0, 7, 0, 4, 0],
#     [0, 9, 8, 0, 0],
#     [0, 0, 0, 0, 0]]

# N,M = 3, 3
# arr = [[0, 0, 0],
# [0, 1, 0],
# [0, 0, 0]]

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]



next_melt = [[0]*M for _ in range(N)]
chunk_map = [[0]*M for _ in range(N)]

chunks = 1
res = 0

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def get_sea_cnt(r, c):
    return sum( 1 for r_t, c_t  in [(r+1, c),(r-1, c), (r, c+1), (r, c-1)] if not arr[r_t][c_t])

def mark_chunk(sr, sc):
    stack = [(sr, sc)]
    chunk_map[sr][sc] = chunks

    while stack:
        r, c = stack.pop()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if arr[nr][nc] > 0 and not chunk_map[nr][nc]:
                chunk_map[nr][nc] = chunks
                stack.append((nr, nc))

def melt_ice():
    for r in range(N):
        for c in range(M):
            arr[r][c] = max(arr[r][c]- next_melt[r][c],0)

while 0 < chunks < 2 :
    chunks = 0
    for r in range(N) :
        for c in range(M) :
            if arr[r][c] <= 0 :
                next_melt[r][c] = 0
                arr[r][c] = 0
            else :
                if not chunk_map[r][c] :
                    chunks += 1
                    mark_chunk(r, c)
                next_melt[r][c] = get_sea_cnt(r, c)

        if chunks > 1 :
            break
    else:
        res += 1
        melt_ice()
        chunk_map = [[0] * M for _ in range(N)]
    if chunks == 0 :
        res = 0


print(f"{res}")
