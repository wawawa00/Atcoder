import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    M = int(next(data))
    count =0
    while M != 0:
        x = N % M
        M = x
        count += 1
    print(count)

if __name__ == '__main__':
    solve()