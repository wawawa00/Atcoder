import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    X = int(next(data))
    S = 'HelloWorld'
    #print(S[X-1])
    S = S[0:X-1] + S[X:len(S)]
    print(S)

if __name__ == '__main__':
    solve()