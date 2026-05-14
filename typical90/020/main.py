import sys
data = iter(sys.stdin.read().split())

a = int(next(data))
b = int(next(data))
c = int(next(data))

if a < c**b:
    print("Yes")
else:
    print("No")