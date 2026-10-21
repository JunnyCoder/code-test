N, M = map(int, input().split())
arr = [set() for _ in range(N)]
for i in range(M):
    s, e = map(int, input().split())
    arr[s].add(e)
    arr[e].add(s)
# print(1 if all( (s+1 in arr[s]) for s in range(N-1)) else 0 )


visited = set()
res = 0
def dfs(start, cnt):
    if cnt == 5 :
        global res 
        res = 1
        return 
    
    for i in arr[start] :
        if i not in visited :
            visited.add(i)
            dfs(i, cnt + 1)
            visited.remove(i)

        if res :
            return

for i in range(N):
    if not res :
        visited.add(i)
        dfs(i,1)
        visited.remove(i)
    else:
        break
        
print(res)