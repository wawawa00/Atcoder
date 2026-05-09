import sys 
data = iter(sys.stdin.read().split())

def solve():
    H = int(next(data))
    W = int(next(data))
    A = [[int(next(data)) for _ in range(W)] for _ in range(H)]
    A_T = [list(x) for x in zip(*A)]

    
    gyou = []
    retu = []

    for i in range(H):
        #print(A[i])
        gyou.append(sum(A[i]))
    for j in range(W):
        #print(A_T[j])
        retu.append(sum(A_T[j]))
    
    for i in range(H):
        goukei = [0]*W
        for j in range(W):
            goukei[j] += gyou[i]+retu[j] - A[i][j]
        print(*goukei)





if __name__ == "__main__":
    solve()