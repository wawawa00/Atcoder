import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    S = next(data)
    N = int(next(data))
    S_cut = S[N:-N]
    print(S_cut)

if __name__ == '__main__':
    solve()