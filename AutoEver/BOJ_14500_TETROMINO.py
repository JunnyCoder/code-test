from itertools import combinations

R, C = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(R)]


dr = [-1,1,0,0]
dc = [0,0,-1,1]

maxV = 0

visited = set()

def dfs(r, c, depth, val):
    global maxV
    if depth == 4:
        if maxV < val :
            maxV = val
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if (nr, nc) not in visited and 0<=nr<R and 0<=nc<C :
            val += arr[nr][nc]
            visited.add((nr,nc))
            dfs(nr, nc, depth+1, val)
            visited.remove((nr,nc))
            val -= arr[nr][nc]

# T 모양은 중심을 기준으로 퍼뜨리는 모양새로 가정한 탬플릿 형태
def template_T(r,c):
    global maxV
    around = []
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<R and 0<=nc<C :
            around.append(arr[nr][nc])
    if len(around) >= 3:
        maxV = max (maxV, max(map(lambda x : sum(x) + arr[r][c], combinations(around, 3))))


for r in range(R) :
    for c in range(C):
        visited.add((r,c))
        dfs(r, c, 1, arr[r][c])
        # T자
        template_T(r,c)
        visited.remove((r,c))


print(maxV)