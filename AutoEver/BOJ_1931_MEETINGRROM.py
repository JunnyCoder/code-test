import heapq

N = int(input())

arr= []
for _ in range(N) :
    a, b = map(int, input().split())
    arr.append((b, a))

heapq.heapify(arr)

last_end = 0
cnt = 0

while arr :
    e, s = heapq.heappop(arr)
    if s >= last_end:
        cnt += 1
        last_end = e


print(cnt)