T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    combo = 1
    ans = [True] * N
    for i in range(1, N+1) :
        if M != 0:
            if N - i >= M:
                if combo == K :
                    ans[N-i] = False
                    combo = 1
                    
                else : 
                    combo += 1
                    M -= 1
            else :
                # print(f"{i} breaked")
                break
                
        else :
            ans[N-i] = False
            # print('here')
    cnt = 0
    multi = 0
    for i in ans :
        if i :
            multi += 1
            cnt += 1
            if multi == K :
                cnt *= 2
                multi = 0    
        else:
            multi = 0
    
    print(f"#{tc} {cnt}")
    # print(N, M, K)
    # print(ans)


