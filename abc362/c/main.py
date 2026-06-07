import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    L = []
    R = []
    ans = []
    
    for _ in range(N):
        Li = int(next(data))
        Ri = int(next(data))
        L.append(Li)
        R.append(Ri)
        ans.append(Ri)
    RminusL = [R[i]-L[i] for i in range(N)]
    #print(RminusL)
    
    if sum(L) > 0 or sum(R) < 0:
        print("No")
    else:
        Xsum = sum(ans)
        print("Yes")
        for i in range(N):
            #print(ans)
            #print(sum(ans))
            #print(RminusL[i])
            if Xsum == 0:
                break
            elif Xsum > RminusL[i]:
                ans[i] -= RminusL[i]
                Xsum -= RminusL[i]
            else:
                ans[i] -= Xsum
                Xsum -= Xsum
        print(*ans)
        


if __name__ == '__main__':
    solve()