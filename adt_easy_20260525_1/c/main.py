import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    xA = int(next(data))
    yA = int(next(data))
    xB = int(next(data))
    yB = int(next(data))
    xC = int(next(data))
    yC = int(next(data))
    AB = (xA-xB)**2 + (yA-yB)**2
    BC = (xB-xC)**2 + (yB-yC)**2
    CA = (xC-xA)**2 + (yC-yA)**2
    if AB == BC + CA or BC == AB + CA or CA == AB + BC:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()