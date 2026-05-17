import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    X = int(next(data))
    Q = int(next(data))
    blackboard = [X]
    for _ in range(Q):
        Ai = int(next(data))
        Bi = int(next(data))
        blackboard.append(Ai)
        blackboard.append(Bi)
    print(blackboard)

if __name__ == '__main__':
    solve()