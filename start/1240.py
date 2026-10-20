T = int(input())
decode_dict ={
    (3,2,1,1) : 0,
    (2,2,2,1) : 1,
    (2,1,2,2) : 2,
    (1,4,1,1) : 3,
    (1,1,3,2) : 4,
    (1,2,3,1) : 5,
    (1,1,1,4) : 6,
    (1,3,1,2) : 7,
    (1,2,1,3) : 8,
    (3,1,1,2) : 9,

}
def decoder (bar) :
    a, c = map(len, "".join(map(str, bar)).replace("1", " ").split())
    b, d = map(len, "".join(map(str, bar)).replace("0", " ").split())
    return decode_dict[(a,b,c,d)]

for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    barcode = list(map(lambda x : 1 if sum(x) else 0, zip(* [map(int, input()) for i in range(N)])))
    pw = [0] * 8

    idx= M -1
    while idx :
        if barcode[idx] :
            secret = barcode[idx - 55 :idx+1]
            break
        idx -= 1
    for i in range(8):
        pw[i] = decoder(secret[7 * i : 7 * (i + 1) ])
    if (sum(pw[::2]) * 3 + sum(pw[1::2])) % 10 == 0 :
        res =sum(pw)
    else :
        res = 0
    print(f"#{test_case} {res}")