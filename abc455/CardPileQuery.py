import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    Q = int(next(data))

    Mt = [[i+1] for i in range(N)]
    Pos = [i+1 for i in range(N)]
    print(Mt)
    print(Pos)
    for _ in range(Q):
        C = int(next(data))
        P = int(next(data))
        


    

if __name__ == '__main__':
    solve()