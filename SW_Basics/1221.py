
T = 10

for test_case in range(1, T + 1):
    _ = input()
    print(f"#{test_case} {sum(map(int, input().split('+')))}")