'''
20분 소요
'''


from collections import deque

T = int(input())

for tc in range(T):
    res = 'error'
    p = list(input())
    N = int(input())
    foo = input()[1:-1]
    if foo :
        arr = deque(list(foo.split(',')))
    else:
        if 'D' in p:
            print(res)
        else :
            print('[]')
        continue

    revese_cnt = 0
    for i in p :
        if i == "R":
            revese_cnt += 1
        else: # D 일 때
            if len(arr) == 0:
                break
            if revese_cnt % 2 == 0 : # 원본 상태, 앞에서 뺄것
                arr.popleft()
            else :
                arr.pop()
    else :
        is_reverse = revese_cnt % 2
        if is_reverse :
            res = '['+','.join(reversed(arr))+']'
        else:
            res = '['+','.join(arr)+']'

    
    print(res)



