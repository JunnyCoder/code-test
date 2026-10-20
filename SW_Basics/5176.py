T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = [0] * (N+1)
    d = {x: [2*x, 2*x+1] for x in range(1, N//2)}
    d[N//2] = [N] if N%2 ==0 else [N-1, N]

    def get_order(start) :
        if start not in d :
            return [start]
        if len(d[start]) == 2 :
            return get_order(d[start][0]) + [start] + get_order(d[start][1])
        else:
            return get_order(d[start][0]) + [start]

    for val, idx in enumerate(get_order(1), 1):
        arr[idx] = val

    print(f"#{test_case} {arr[1]} {arr[N//2]}")



#          6
#    4           8
#  2   5      7      9
# 1  3

#        5
#    3           7
#  2   4      6     8
# 1

#            8
#     4                12
#  2       6       10        14
# 1  3   5  7    9   11   13    15
