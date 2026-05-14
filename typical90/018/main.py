import sys
import math
data = iter(sys.stdin.read().split())

T = int(next(data))
L = int(next(data))
X = int(next(data))
Y = int(next(data))
Q = int(next(data))

for _ in range(Q):
    E = int(next(data))
    theta = E / T * 2 * math.pi
    #print(theta)
    sin = math.sin(theta)

    hukaku = math.atan2((L/2-L/2*math.cos(theta)),math.sqrt(X**2+(Y+L/2*math.sin(theta))**2))
    print(f"{math.degrees(hukaku):.12f}")