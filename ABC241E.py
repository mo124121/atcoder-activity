N, K = map(int, input().split())
A = list(map(int, input().split()))

seen = set()
seen.add(0)
x = 0
trans = [0]
for _ in range(N):
    x += A[x % N]

    if x % N in seen:
        break
    trans.append(x % N)
    seen.add(x % N)
z = trans.index(x % N)

ret = 0
if K < z:
    for t in trans[:K]:
        ret += A[t]
else:
    for t in trans[:z]:
        ret += A[t]
    cycle = len(trans) - z
    loop_sum = 0
    for t in trans[z:]:
        loop_sum += A[t]
    ret += loop_sum * ((K - z) // cycle)
    for t in trans[z : z + (K - z) % cycle]:
        ret += A[t]
print(ret)

"""
K回の操作の中で、各要素何回出てきますか？という問題
ダンプリングくさい、が実装は忘れた
"""
