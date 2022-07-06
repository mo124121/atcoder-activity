from collections import Counter


N = int(input())
A = list(map(int, input().split()))

count = Counter(A)
B = [k for k in count.keys()]
cand = set(B)

B.sort()
M = max(B)

for b in B:
    if b in cand:
        j = b * 2
        while j <= M:
            cand.discard(j)
            j += b

for k, v in count.items():
    if v != 1:
        cand.discard(k)

print(len(cand))


"""
全組み合わせをすれば確認可能 N**2

ソートしてふるいにかけていけばよいのでは？
小さいのの倍数として出てきたものはもうみなくていい

2個以上でたのは飛ばす


"""
