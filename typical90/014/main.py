import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    A = [int(next(data)) for _ in range(N)]
    B = [int(next(data)) for _ in range(N)]

    A_sorted = sorted(A)
    B_sorted = sorted(B)

    icv = 0

    for i in range(N):
        icv += abs(A_sorted[i]-B_sorted[i])
    
    print(icv)

if __name__ == '__main__':
    solve()