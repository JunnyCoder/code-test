N, M = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
r = M -1
while l < r :
    if arr[l] < arr[r]:
        pass