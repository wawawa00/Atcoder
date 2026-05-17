import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    S = next(data)
    N = len(S)
    isC = []
    count = 0
    for i, char in enumerate(S):
        if char == "C" and i == 0:
            count += 1
        elif char == "C" and i == N-1:
            count += 1
        elif char == "C":
            bubunlen = min(i+1 -1, N-(i+1))
            count += bubunlen+1
    print(count)
    


if __name__ == '__main__':
    solve()