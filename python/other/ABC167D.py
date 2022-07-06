N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

way = [1]
seen = set([1])
pos = 1
for i in range(N):
    pos = A[pos]
    if pos in seen:
        break
    way.append(pos)
    seen.add(pos)
enter = way.index(pos)

if K < enter:
    ret = way[K]
else:
    l = len(way) - enter
    i = (K - enter) % l
    ret = way[enter + i]
print(ret)


"""
ループ検知実装
"""
