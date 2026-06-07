import sys 
data = iter(sys.stdin.read().split())
N = int(next(data))
K = int(next(data))

prime_count = [0]*(N+1)

for i in range(2, N+1):
    if prime_count[i] == 0:
        #print(prime_count[i])
        for j in range(i, N+1, i):
            #print(j)
            prime_count[j] += 1
ans = 0
for i in range(2, N+1):
    if prime_count[i] >= K:
        ans += 1
print(ans)