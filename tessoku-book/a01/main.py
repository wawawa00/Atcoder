import sys
sys.setrecursionlimit(2000000)
def solve():
    data = sys.stdin.read().split()
    if not data: return

    N = int(data[0])

    print(N ** 2)

if __name__ == '__main__':
    solve()