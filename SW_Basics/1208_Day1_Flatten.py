'''

한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.




가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업을 덤프라고 정의한다.

위의 예시에서 제1회 덤프를 수행한 이후 화면은 다음과 같다.



A부분의 상자를 가장 낮은 B부분에 덤프하였으며, A대신 A’부분의 상자를 사용해도 무방하다.

다음은 제2회 덤프를 수행한 이후의 화면이다.



A’부분의 상자를 옮겨서, C부분에 덤프하였다. 이때 C 대신 C’부분에 덤프해도 무방하다.

2회의 덤프 후, 최고점과 최저점의 차이는 8 – 2 = 6 이 되었다 (최초덤프 이전에는 9 – 1 = 8 이었다).

덤프 횟수가 2회로 제한된다면, 이 예시 문제의 정답은 6이 된다.

[제약 사항]

가로 길이는 항상 100으로 주어진다.

모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.

덤프 횟수는 1이상 1000이하로 주어진다.

주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다).

[입력]

총 10개의 테스트 케이스가 주어지며, 각 테스트 케이스의 첫 번째 줄에는 덤프 횟수가 주어진다. 그리고 다음 줄에 각 상자의 높이값이 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 최고점과 최저점의 높이 차를 출력한다.

'''

'''
카운팅 배열 응용 풀이
'''
T = 10

for test_case in range(1, T + 1):
    dumps = int(input())
    arr = list(map(int, input().split()))

    counting_arr = [0 for _ in range(101)]
    minV = 100
    maxV = 0

    for i in arr:
        counting_arr[i] += 1
        minV = i if i < minV else minV
        maxV = i if maxV < i else maxV

    for _ in range(dumps):
        counting_arr[minV] -= 1
        counting_arr[minV + 1] += 1
        minV = minV + 1 if counting_arr[minV] == 0 else minV

        counting_arr[maxV] -= 1
        counting_arr[maxV - 1] += 1
        maxV = maxV - 1 if counting_arr[maxV] == 0 else maxV

        if maxV - minV <= 1:
            break
    print(f"#{test_case} {maxV - minV}")




T = 10

for test_case in range(1, T + 1):
    dumps = int(input())
    arr = list(map(int, input().split()))

    for _ in range(dumps ):
        maxidx = arr.index(max(arr))
        minidx = arr.index(min(arr))
        if arr[maxidx] - arr[minidx] > 1:
            arr[maxidx] -= 1
            arr[minidx] += 1
        else :
            break

    print(f"#{test_case} {arr[arr.index(max(arr))] - arr[arr.index(min(arr))]}")





T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    stations = sorted(list(map(int, input().split())), reverse=True)
    stations.append(0)
    last_charge = N
    temp = last_charge
    cnt = 0
    for i in stations :
        if temp - i > K :
            cnt = 0
            break
        else:
            if last_charge - i > K :
                last_charge = temp
                cnt += 1
            temp = i

    print(f"#{test_case} {cnt}")



from collections import defaultdict

T = int(input())


for test_case in range(1, T + 1):
    N = input()
    dd = defaultdict(int)
    maxval = None
    maxcnt = 0
    for i in N :
        dd[i] += 1
        if dd[i] > maxcnt :
            maxval = i
            maxcnt = dd[i]

    print(f"#{test_case} {maxval} {maxcnt}")



T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    buses = [tuple(map(int,input().split())) for _ in range(N)]
    P = int(input())
    stations = [int(input()) for _ in range(P)]
    counter = [0] * P
    for st_min, st_max in buses :
        for i, v in enumerate(stations) :
            if st_min <= v <= st_max :
                counter[i] += 1
    print(f"#{test_case} ", end="")
    for i in counter :
        print(i, end=" ")
    print()

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    # accumulate_sum = [sum(arr[i:i+m]) for i in range(n-m + 1)]
    # min_sum = min(accumulate_sum)
    # max_sum = max(accumulate_sum)
    accumulate_sum = [arr[i:i + m] for i in range(n - m + 1)]

    tempsum = 0
    for i in accumulate_sum[0]:
        tempsum += i
    min_sum = i
    max_sum = i

    for a in accumulate_sum[1:]:
        tempsum = 0
        for i in a:
            tempsum += i
        min_sum = min(accumulate_sum)
        max_sum = max(accumulate_sum)
    print(f"#{test_case} {max_sum - min_sum}")

T = 10

for test_case in range(1, T + 1):
    dumps = int(input())
    arr = list(map(int, input().split()))

    max_idx = 0
    min_idx = 0

    for _ in range(dumps ):
        maxV = arr[0]
        minV = arr[0]
        for i in range(100) :
            min_idx, minV = (i, arr[i]) if arr[i] < minV else (min_idx, minV)
            max_idx, maxV = (i, arr[i]) if arr[i] > maxV else (max_idx, maxV)
        print(min_idx, max_idx)
        if arr[max_idx] - arr[min_idx] > 1:
            arr[min_idx] += 1
            arr[max_idx] -= 1
        else :
            break


    minV = arr[0]
    maxV = arr[0]

    for i in range(100) :
        min_idx, minV = (i, arr[i]) if arr[i] < minV else (min_idx, minV)
        max_idx, maxV = (i, arr[i]) if arr[i] > maxV else (max_idx, maxV)

    print(f"#{test_case} {maxV} {minV}")
