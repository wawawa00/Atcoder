import sys
data = iter(sys.stdin.read().split())

N = int(next(data))
K = int(next(data))
H = [int(next(data)) for _ in range(N)]

dp = [float("inf") for _ in range(N)]
dp[0] = 0

for i in range(N):
    for k in range(1, K+1):
        if i + k > N - 1:
            break
        
        dp[i+k] = min(dp[i+k], dp[i]+abs(H[i+k]-H[i]))

print(dp[N-1])