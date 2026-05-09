import sys

def solve():
    data = iter(sys.stdin.read().split())

    N = int(next(data))
    Q = int(next(data))
    A = [int(next(data)) for _ in range(N)]

    S = [0]*(N + 1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    
    for _ in range(Q):
        l = int(next(data))
        r = int(next(data))
        print(S[r] - S[l-1])

    


    
if __name__ == '__main__':
    solve()