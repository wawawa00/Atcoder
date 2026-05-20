import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    X = int(next(data))
    Q = int(next(data))
    tyuuou = X
    tyuuou_minus = 0
    tyuuou_plus = 0
    A1 = int(next(data))
    B1 = int(next(data))
    if max(A1,B1) <= tyuuou:
        tyuuou = max(A1,B1)
        tyuuou_plus = tyuuou
        tyuuou_minus = min(A1, B1)
    elif min(A1,B1) >= tyuuou:
        tyuuou = min(A1, B1)
        tyuuou_plus = max(A1, B1)
        tyuuou_minus = tyuuou
    
    for _ in range(Q-1):
        Ai = int(next(data))
        Bi = int(next(data))

        big = max(Ai, Bi)
        sma = min(Ai, Bi)
        if big <= tyuuou:
            tyuuou = tyuuou_minus
            tyuuou_plus 



if __name__ == '__main__':
    solve()