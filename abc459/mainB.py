import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    S = [next(data) for _ in range(N)]
    C = []

    for s in S:
        if s[0] == 'a' or s[0] == 'b' or s[0] == 'c':
            C.append('2')
        elif s[0] == 'd' or s[0] == 'e' or s[0] == 'f':
            C.append('3')
        elif s[0] == 'g' or s[0] == 'h' or s[0] == 'i':
            C.append('4')
        elif s[0] == 'j' or s[0] == 'k' or s[0] == 'l':
            C.append('5')
        elif s[0] == 'm' or s[0] == 'n' or s[0] == 'o':
            C.append('6')
        elif s[0] == 'p' or s[0] == 'q' or s[0] == 'r' or s[0] == 's':
            C.append('7')
        elif s[0] == 't' or s[0] == 'u' or s[0] == 'v':
            C.append('8')
        elif s[0] == 'w' or s[0] == 'x' or s[0] == 'y' or s[0] == 'z':
            C.append('9')
    print("".join(C))
if __name__ == '__main__':
    solve()