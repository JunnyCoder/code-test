# 1221. [S/W 문제해결 기본] 5일차 - GNS


alien_nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]


T = int(input())

for test_case in range(1, T + 1):
    N = int(input().split()[1])
    arr = list(input().split())
    counting_arr = [0] * 10
    for i in arr :
        counting_arr[alien_nums.index(i)] += 1

    s = " ".join( (v+" ") * counting_arr[i] for i,v in enumerate(alien_nums))
    print(f"#{test_case}")
    print(s)




    # arr.sort(key = lambda x : alien_nums.index(x))
    # print(f"#{test_case}")
    # print(" ".join(arr))