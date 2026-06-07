import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    K = int(next(data))
    M = int(next(data))
    jew = []

    for i in range(N):
        Ci = int(next(data))
        Vi = int(next(data))
        jew.append((Ci,Vi))

    color_num = 0
    color_set = set()
    select = []
    value = 0
    jew = sorted(jew, key=lambda x: -x[1])

    #print(jew)
    for i in range(N):
        if len(select) == K:
            break
        elif M - color_num == K - len(select) and jew[i][0] in color_set:
            continue
        else:
            select.append(jew[i])
            value += jew[i][1]
            if jew[i][0] not in color_set:
                color_set.add(jew[i][0])
                color_num += 1
        
        #print(select)
    
    print(value)

if __name__ == '__main__':
    solve()