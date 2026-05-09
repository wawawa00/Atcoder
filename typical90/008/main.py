import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    S = next(data)

    tail = {'a':0, 't':0, 'c':0, 'o':0, 'd':0, 'e':0, 'r':0}
    MOD = 10**9+7
    
    for char in S:
        if char == 'a':
            tail['a'] += 1
        elif char == 't':
            tail['t'] += tail['a']
        elif char == 'c':
            tail['c'] += tail['t']
        elif char == 'o':
            tail['o'] += tail['c']
        elif char == 'd':
            tail['d'] += tail['o']
        elif char == 'e':
            tail['e'] += tail['d']
        elif char == 'r':
            tail['r'] += tail['e']
    
    print(tail['r']%MOD)


if __name__ == '__main__':
    solve()