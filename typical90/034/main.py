import sys
from collections import defaultdict
data = iter(sys.stdin.read().split())

N = int(next(data))
K = int(next(data))
A = [int(next(data)) for _ in range(N)]

inside_count = defaultdict(int)

maxlen = 0
left = 0

for right in range(N):
    inside_count[A[right]] += 1

    while len(inside_count) > K:
        inside_count[A[left]] -= 1

        if inside_count[A[left]] == 0:
            del inside_count[A[left]]
        
        left += 1
    
    if right - left + 1 > maxlen:
        maxlen = right - left + 1

print(maxlen)