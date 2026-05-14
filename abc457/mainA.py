import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    A = [int(next(data)) for _ in range(N)]
    X = int(next(data))

    print(A[X-1])

if __name__ == '__main__':
    solve()