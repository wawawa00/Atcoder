import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    L = []
    A = []

    for _ in range(N):
        Li = int(next(data))
        Ai = [int(next(data)) for _ in range(Li)]
        L.append(Li)
        A.append(Ai)
    
    X = int(next(data))
    Y = int(next(data))

    print(A[X-1][Y-1])
if __name__ == '__main__':
    solve()