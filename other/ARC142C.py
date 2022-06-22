from collections import defaultdict


N = int(input())

dist = defaultdict(list)
# 各距離の確認
for i in range(3, N + 1):
    print(f"? 1 {i}", flush=True)
    d1 = int(input())
    print(f"? 2 {i}", flush=True)
    d2 = int(input())
    d = d1 + d2
    dist[d].append(i)

# 最短のもののサーチ
dmin = 10**10
for k in dist.keys():
    dmin = min(dmin, k)

l = len(dist[dmin])
if dmin != 3:
    print(f"! {dmin}", flush=True)
    exit()

if l != 2:
    print(f"! 1", flush=True)
    exit()

# 内外の確認
l = dist[dmin][0]
r = dist[dmin][1]
print(f"? {l} {r}", flush=True)
dlr = int(input())
if dlr == 1:
    print(f"! 3", flush=True)
else:
    print(f"! 1", flush=True)
