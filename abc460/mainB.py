import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    T = int(next(data))
    for _ in range(T):
        X1 = int(next(data))
        Y1 = int(next(data))
        R1 = int(next(data))
        X2 = int(next(data))
        Y2 = int(next(data))
        R2 = int(next(data))
        d2 = (X1-X2)**2 + (Y1-Y2)**2
        if d2 > (R1+R2)**2:
            print("No")
        elif d2 < (R1-R2)**2:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    solve()