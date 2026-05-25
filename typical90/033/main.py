import sys

data = iter(sys.stdin.read().split())

H = int(next(data))
W = int(next(data))

if H == 1 or W == 1:
    print(H*W)

else:
    tate = -((-H)//2)
    #print(tate)
    yoko = -(-(W)//2)
    #print(yoko)
    print(tate*yoko)