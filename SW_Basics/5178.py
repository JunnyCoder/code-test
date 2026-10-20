
T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = [0] * (N+1)

    for _ in range(M) :
        n, v = map(int, input().split())
        arr[n] = v
        while n > 0 :
            n //= 2
            arr[n] += v

    print(f"#{test_case} {arr[L]}")
