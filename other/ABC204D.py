N = int(input())
T = list(map(int, input().split()))
tot = sum(T)
seen = set()
seen.add(0)
for t in T:
    tmp = set()
    for v in seen:
        tmp.add(v + t)
    seen.update(tmp)

ret = 10**8

for t in seen:
    ret = min(ret, max(t, tot - t))

print(ret)

"""
非初見
貪欲法はトラップがあった気がする
合計値を記憶しておいて、
到達可能なところを探し、最も差が小さいものを探す
"""
