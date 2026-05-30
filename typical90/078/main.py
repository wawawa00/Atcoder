import sys
from collections import defaultdict
data = iter(sys.stdin.read().split())

N = int(next(data))
M = int(next(data))
d = defaultdict(set)
for _ in range(M):
    a = int(next(data))
    b = int(next(data))
    key = max(a, b)
    value = min(a, b)
    d[key].add(value)
count = 0
for i in range(1, N+1):
    if len(d[i]) == 1:
        count += 1

print(count)
