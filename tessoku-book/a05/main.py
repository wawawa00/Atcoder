import sys
def solve():
    data = sys.stdin.read().split()
    if not data: return

    N = int(data[0])
    K = int(data[1])
    count = 0

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if 1 <= K - i - j <= N:
                count += 1

    print(count)

if __name__ == '__main__':
    solve()