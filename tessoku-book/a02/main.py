import sys
sys.setrecursionlimit(2000000)
def solve():
    data = sys.stdin.read().split()
    if not data: return

    N = int(data[0])
    X = int(data[1])

    A = list(map(int, data[2:]))

    count = 0

    for i in range(N):
        if A[i] == X:
            count += 1
        else:
            continue
    if count > 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    solve()