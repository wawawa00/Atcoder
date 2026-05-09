import sys
def solve():
    data = iter(sys.stdin.read().split())
    S = next(data)
    MOD = 998244353
    dp = {'a':0, 'b':0, 'c':0}

    for s in S:
        other_sum = 0
        for char in 'abc':
            if s != char:
                other_sum += dp[char]
        dp[s] += (1 + other_sum)%MOD
    
    print(sum(dp.values())%MOD)
if __name__ == '__main__':
    solve()