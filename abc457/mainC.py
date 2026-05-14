import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    K = int(next(data))
    L = []
    A = []
    for _ in range(N):
        Li = int(next(data))
        Ai = [int(next(data)) for _ in range(Li)]
        L.append(Li)
        A.append(Ai)
    C = []
    for _ in range(N):
        Ci = int(next(data))
        C.append(Ci)
    
    B_index = 0
    A_index = 0
    for i in range(N):
        if B_index + C[i]*L[i] > K:
            break
        if B_index + C[i]*L[i] == K:
            return print(A[i][-1])
        A_index = i + 1
        B_index += C[i]*L[i]
    print(A[A_index][(K-B_index)%L[A_index]-1])
if __name__ == '__main__':
    solve()