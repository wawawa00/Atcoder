import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return
    X = int(next(data))

    dice = []
    for i in range(6):
        for j in range(6):
            for k in range(6):
                dice.append(i + j + k + 3)
    
    if X in dice:
        print("Yes")
    else:
        print("No")

    

if __name__ == '__main__':
    solve()