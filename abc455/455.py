import sys

def solve():
    data = iter(sys.stdin.read().split())

    A = int(next(data))
    B = int(next(data))
    C = int(next(data))

    if A != B and B == C:
        print("Yes")
    else:
        print("No")
    
if __name__ == "__main__":
    solve()
