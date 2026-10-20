T = 10
calc_dict = {
    "+" : lambda a, b : int(a)+int(b),
    "-" : lambda a, b : int(a)-int(b),
    "*" : lambda a, b : int(a)*int(b),
    "/" : lambda a, b : int(a)//int(b)
}

for test_case in range(1, T + 1):
    N = int(input())
    edges = {}
    for _ in range(N) :
        temp = list(input().split())
        edges[int(temp[0])] = {"V" : temp[1],
                               "L" : 0,
                               "R" : 0
                               }
        if len(temp) == 4 :
            edges[int(temp[0])]["L"] = int(temp[2])
            edges[int(temp[0])]["R"] = int(temp[3])

    def calculator(curr) :
        V, L, R = edges[curr]["V"], edges[curr]["L"], edges[curr]["R"]
        if V in calc_dict:
            return calc_dict[V](calculator(L), calculator(R))
        else :
            return V
    print(f"#{test_case} {calculator(1)}")