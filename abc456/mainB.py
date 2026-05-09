import sys
import collections
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    D1 = [int(next(data)) for _ in range(6)]
    D2 = [int(next(data)) for _ in range(6)]
    D3 = [int(next(data)) for _ in range(6)]
    
    set1 = set(D1)
    set2 = set(D2)
    set3 = set(D3)

    exist_14 = False
    exist_15 = False
    exist_16 = False

    exist_24 = False
    exist_25 = False
    exist_26 = False

    exist_34 = False
    exist_35 = False
    exist_36 = False

    for x in D1:
        if x == 4:
            exist_14 += 1
        elif x == 5:
            exist_15 += 1
        elif x == 6:
            exist_16 += 1
        else:
            continue
    for x in D2:
        if x == 4:
            exist_24 += 1
        elif x == 5:
            exist_25 += 1
        elif x == 6:
            exist_26 += 1
        else:
            continue
    for x in D3:
        if x == 4:
            exist_34 += 1
        elif x == 5:
            exist_35 += 1
        elif x == 6:
            exist_36 += 1
        else:
            continue
    
    P_456 = 0
    P_465 = 0
    P_546 = 0
    P_564 = 0
    P_645 = 0
    P_654 = 0

    if exist_14>0 and exist_25>0 and exist_36>0:
        P_456 = (exist_14*exist_25*exist_36) / 216
    if exist_14>0 and exist_26>0 and exist_35>0:
        P_465 = (exist_14*exist_26*exist_35) / 216
    if exist_15>0 and exist_24>0 and exist_36>0:
        P_546 = (exist_15*exist_24*exist_36) / 216
    if exist_15>0 and exist_26>0 and exist_34>0:
        P_564 = (exist_15*exist_26*exist_34) / 216
    if exist_16>0 and exist_24>0 and exist_35>0:
        P_645 = (exist_16*exist_24*exist_35) / 216
    if exist_16>0 and exist_25>0 and exist_34>0:
        P_654 = (exist_16*exist_25*exist_34) / 216
    print((P_456+P_465+P_546+P_564+P_645+P_654))

    
if __name__ == '__main__':
    solve()