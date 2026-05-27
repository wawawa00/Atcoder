import sys
from collections import defaultdict

data = iter(sys.stdin.read().split())
N = int(next(data))
A = [int(next(data)) for _ in range(N)]


for s in range(N):
    idx, Ai = s, A[s]

