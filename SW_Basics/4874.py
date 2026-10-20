from collections import deque

def calc(op, a, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a // b
    raise Exception


T = int(input())

for test_case in range(1, T + 1):
    arr = list(input().split())
    num_stack = []
    res = "error"
    for i in arr :
        try :
            num_stack.append(int(i))
        except Exception :
            try :
                if i == "." :
                    res = num_stack.pop()
                else :
                    b = num_stack.pop()
                    a = num_stack.pop()
                    num_stack.append(calc(i, a, b))
            except Exception :
                break
    if not num_stack :
        res = 'error'

    print(f"#{test_case} {res}")