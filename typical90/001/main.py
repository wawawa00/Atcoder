import sys

data = iter(sys.stdin.read().split())

def solve():
    N = int(next(data))
    L = int(next(data))
    K = int(next(data))

    A = [int(next(data)) for _ in range(N)]

    
