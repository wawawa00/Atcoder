import sys
def solve():
    data = iter(sys.stdin.read().split())
    S = next(data)
    N = len(S)
    if not data:
        return
    if N == 1:
        print(1)
        return
    # 隣り合っていたらTrueあっていなかったらFalse
    nei = [False for _ in range(N)]
    for i in range(N):
        if i == 0 and S[i] == S[i+1]:
            nei[i] = True
        elif i == N-1:
            if S[i] == S[i-1]:
                nei[i] = True
            else:
                break
        elif S[i] == S[i+1] or S[i] == S[i-1]:
            nei[i] = True

    partial = []
    count = 0
    for i in range(N):
        if i == 0:
            count +=1
        elif i == N-1:
            if S[i] == S[i-1]:
                partial.append(count)
                partial.append(1)
            else:
                partial.append(count+1)
        elif nei[i] and nei[i-1] and S[i] == S[i-1]:
            partial.append(count)
            count = 1
        else: 
            count += 1
    
    answer = 0
    for x in partial:
        answer += (x*(x+1))/2
    print(int(answer)%998244353)

        


    

if __name__ == '__main__':
    solve()