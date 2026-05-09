import sys
data = iter(sys.stdin.read().split())

def solve():
    N = int(next(data))
    Q = int(next(data))
    coordinate = [(i+1, 0) for i in range(N)][::-1]

    for _ in range(Q):
        Q1 = int(next(data))
        Q2 = next(data)
        x, y = coordinate[-1]

        if Q1 == 1 and Q2 == 'R':
            x += 1
            coordinate.append((x, y))
        
        elif Q1 == 1 and Q2 == 'L':
            x -= 1
            coordinate.append((x, y))
        
        elif Q1 == 1 and Q2 == 'U':
            y += 1
            coordinate.append((x, y))
        
        elif Q1 == 1 and Q2 == 'D':
            y -= 1
            coordinate.append((x, y))
        
        else:
            Q2 = int(Q2)
            print(coordinate[len(coordinate)-Q2][0], coordinate[len(coordinate)-Q2][1])
        
        

if __name__ == "__main__":
    solve()