import sys

data=iter(sys.stdin.read().split())
N=int(next(data))
H=[int(next(data)) for _ in range(N)]
dp=[float('inf') for _ in range(N)]
dp[0]=0
for i in range(N-2):
  if dp[i]==float('inf'):
    continue
  else:
    if dp[i+1] > dp[i] + abs(H[i]-H[i+1]):
      dp[i+1] = dp[i] + abs(H[i]-H[i+1])
    if dp[i+2] > dp[i] + abs(H[i]-H[i+2]):
      dp[i+2] = dp[i] + abs(H[i]-H[i+2])

if dp[N-1] > dp[N-2] + abs(H[N-2]-H[N-1]):
  dp[N-1] =dp[N-2] + abs(H[N-2]-H[N-1])

print(dp[N-1])