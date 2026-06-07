import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    A = int(next(data))
    D = int(next(data))
    if A <= D:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()