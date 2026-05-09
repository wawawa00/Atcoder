import sys

def solve():
    data = iter(sys.stdin.read().split())

    H = int(next(data))
    W = int(next(data))

    X = [[int(next(data)) for _ in range(W)] for _ in range(H)]

    Q = int(next(data))

    S = [[0] * (W+1) for _ in range(H+1)]
    
    
    for i in range(1, H + 1):
        for j in range(1, W + 1):
             S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + X[i-1][j-1]
            

    for _ in range(Q):
        A = int(next(data))
        B = int(next(data))
        C = int(next(data))
        D = int(next(data))

        count = S[C][D] + S[A-1][B-1] - S[A-1][D] - S[C][B-1]
        print(count)
        


if __name__ == "__main__":
    solve()