
from itertools import accumulate

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    mul_arr = set()

    for i in range(1, N+1):
        mul_arr.update(set(j * k for (j, k) in zip(arr, arr[i:])))
    print(list(mul_arr))
    # mul_arr.sort(reverse=True)

    big_num = -1
    for i in list(mul_arr):
        if list(str(i)) == sorted(str(i)):
            big_num = max(big_num, i)


    print(f"#{test_case} {big_num}")