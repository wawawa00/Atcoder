import sys

def solve():
    data = iter(sys.stdin.read().split())
    
    D = int(next(data))
    N = int(next(data))
    number = 0

    people = [0]*(D+2)

    for _ in range(N):
        l = int(next(data))
        r = int(next(data))
        
        people[l] += 1
        people[r+1] += -1
    
    for i in range(D):
        number += people[i + 1]
        print(number)

    



if __name__ == "__main__":
    solve()