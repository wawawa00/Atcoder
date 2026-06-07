import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    A = [int(next(data)) for _ in range(N)]
    B = [int(next(data)) for _ in range(N)]
    bool = False
    for i in range(N):
        if i != B[A[i]-1]-1:
            bool = True
            break
    if bool:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    solve()