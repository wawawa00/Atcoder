import sys
data = iter(sys.stdin.read().split())

N = int(next(data))
vacation = {'a':0, 'b':0, 'c':0}

for i in range(N):
    #print(vacation)
    ai = int(next(data))
    bi = int(next(data))
    ci = int(next(data))
    if i == 0:
        vacation['a'] = ai
        vacation['b'] = bi
        vacation['c'] = ci
        continue
    a = vacation['a']
    b = vacation['b']
    c = vacation['c']
    vacation['a'] = max(b, c) + ai
    vacation['b'] = max(a, c) + bi
    vacation['c'] = max(a, b) + ci

print(max(vacation.values()))