# 5185. [S/W 문제해결 구현] 1일차 - 이진수

T = int(input())

for test_case in range(1, T + 1):
    _, s = input().split()
    print(f"#{test_case} {"".join(map(lambda x : f"{int(x, 16):04b}", s))}")

#
# # 5186. [S/W 문제해결 구현] 1일차 - 이진수2
#
# bins = [2 ** (-i) for i in range(1,13)]
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     n = float(input())
#     res = ""
#     for b in bins :
#         if n - b >= 0 :
#             res = res + "1"
#             n -= b
#             if n == 0 :
#                 break
#         else :
#             res = res + "0"
#
#     if n!= 0 :
#         res ="overflow"
#     print(f"#{test_case} {res}")

#
# a01000001110110100001011011001101
# a01000001110110100001011011001101