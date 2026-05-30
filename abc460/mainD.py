import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    H = int(next(data))
    W = int(next(data))
    maxcount = 0
    hukyuu = 0
    Switch = False
    S = [next(data) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.' and not Switch:
                Switch = True
                r = i
                c = j
            #elif 

if __name__ == '__main__':
    solve()