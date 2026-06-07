import sys
from collections import Counter
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    A = [int(next(data)) for _ in range(N)]
    A_sorted = sorted(A)
    M = max(A)
    is_prime = [True] * (M+1)
    is_prime[0] = False
    count = [0] * (M+1)
    for i in A_sorted:
        count[i] += 1
        if is_prime[i]:
            for j in range(i*2, len(is_prime), i):
                is_prime[j]=False
    ans = 0
    #print(is_prime)
    for i in range(N):
        if is_prime[A[i]] and count[A[i]] == 1:
            ans += 1
    print(ans)
if __name__ == '__main__':
    solve()