import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    C = [0]*N
    P = [0]*N
    S = [0]*(N+1)
    S_2 = [0]*(N+1)
    sum = 0
    sum_2 = 0
    for i in range(N):
        C_i = int(next(data))
        P_i = int(next(data))
        C[i] = C_i
        P[i] = P_i
        sum += P_i
        S[i+1] = sum
        sum_2 += P_i*(C_i-1)
        S_2[i+1] = sum_2

    Q = int(next(data))

    for i in range(Q):
        L = int(next(data))
        R = int(next(data))
        S_LR = S[R] - S[L-1]
        S_2LR = S_2[R] - S_2[L-1]
        print(S_LR-S_2LR, S_2LR)
        


if __name__ == '__main__':
    solve()