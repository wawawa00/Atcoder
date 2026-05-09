import sys

def solve():
    data = iter(sys.stdin.read().split())

    H = int(next(data))
    W = int(next(data))
    N = int(next(data))


    for _ in range(N):
        A = int(next(data))
        B = int(next(data))
        C = int(next(data))
        D = int(next(data))
        