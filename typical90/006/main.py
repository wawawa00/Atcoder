import sys
data = iter(sys.stdin.read().split())

N = int(next(data))
K = int(next(data))
S = list(next(data))
dic = {}
for i, v in enumerate(S):
    dic[i] = v
dict_sorted = sorted(dic.items(), key=lambda x:x[1])

print(dict_sorted)
dict_K = dict(dict_sorted[:K])
print(dict_K)
dict_K_sorted = sorted(dict_K.items(), key=lambda x:x[0])

print(dict_K_sorted)
