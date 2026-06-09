import sys

def count_K_ika(A, K):
    if K < 0:
        return 0
    now = 0
    left = 0
    ans = 0

    for right in range(len(A)):
        now += A[right]
        while now > K:
            now -= A[left]
            left += 1
        ans += right - left + 1

    return ans

def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    H = int(next(data))
    W = int(next(data))
    K = int(next(data))
    grid = [next(data) for _ in range(H)]
    
    if H > W:
        grid = [list(row) for row in zip(*grid)]
        H, W = W, H


    ans = 0
    for top in range(H):
        col_sum = [0]*W
        for bottom in range(top, H):
            for col in range(W):
                col_sum[col] += int(grid[bottom][col])
            ans += count_K_ika(col_sum, K) - count_K_ika(col_sum, K - 1)

    print(ans)
if __name__ == '__main__':
    solve()