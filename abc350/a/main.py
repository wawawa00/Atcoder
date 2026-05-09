import sys
sys.setrecursionlimit(2000000)
def solve():
    data = sys.stdin.read().split()
    if not data: return

    S = data[0]
    count = int(S[3:])

    if count == 316:
        print("No")

    elif 0 < count and count < 350:
        print("Yes")

    else:
        print("No")
    
    

if __name__ == '__main__':
    solve()