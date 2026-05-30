import sys
data = iter(sys.stdin.read().split())

N = int(next(data))
W = int(next(data))
dp = [-float('inf')]*(W+1)
dp[0] = 0

for _ in range(N):
    print(dp)
    wi = int(next(data))
    vi = int(next(data))
    seen = []
    for i in range(W):
        if dp[i] == -float('inf'):
            continue
        elif i + wi <= W and i not in seen:
            dp[i+wi] = max(dp[i+wi], dp[i]+vi)
            seen.append(i+wi)

print(max(dp))
