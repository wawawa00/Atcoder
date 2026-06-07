import sys
from collections import defaultdict
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    H = int(next(data))
    W = int(next(data))
    K = int(next(data))
    grid = [next(data) for _ in range(H)]
    grid_sum = [[]]*H
    retu_sum = []
    retu = [0]*W
    for i in range(H):
        for j in range(W):
            retu[j] += int(grid[i][j])
        #print(retu)
        retu_sum.append(retu[:])
    
    for i in range(H):
        grid_ij = 0
        grid_i = []
        #print(retu_sum)
        for j in range(W):
            grid_ij += retu_sum[i][j]
            grid_i.append(grid_ij)
        grid_sum[i] = grid_i
    
    def rect_sum(top, left, bottom, right):
        res = grid_sum[bottom][right]

        if top > 0:
            res -= grid_sum[top-1][right]
        if left > 0:
            res -= grid_sum[bottom][left-1]
        if top > 0 and left > 0:
            res += grid_sum[top-1][left-1]
        return res

    ans = 0
    for top in range(H):
        for bottom in range(top, H):
            count = defaultdict(int)
            count[0] = 1
            s = 0
            for col in range(W):
                x = rect_sum(top, col, bottom, col)
                s += x

                ans += count[s-K]
                count[s] += 1
            
    print(ans)
if __name__ == '__main__':
    solve()