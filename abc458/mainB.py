import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    H = int(next(data))
    W = int(next(data))
    X = [[0]*W for _ in range(H)]

    if H == 1 and W==1:
        X = [[0]]
    elif H==1:
        for j in range(W):
            if j==0 or j==W-1:
                X[0][j] = 1
            else:
                X[0][j] = 2
    elif W==1:
        for i in range(H):
            if i == 0 or i == H-1:
                X[i][0] = 1
            else:
                X[i][0] = 2

    else:
        for i in range(H):
            for j in range(W):
                if i - 1 >=0 and i + 1 <= H-1 and j-1 >=0 and j+1 <= W-1:
                    X[i][j] += 4
                elif i - 1 >=0 and i + 1 <= H-1:
                    X[i][j] += 3
                elif j-1 >=0 and j+1 <= W-1:
                    X[i][j] += 3
                else:
                    X[i][j] += 2
    
    for i in range(H):
        print(' '.join(list(map(str,X[i]))))
            

            
                

if __name__ == '__main__':
    solve()