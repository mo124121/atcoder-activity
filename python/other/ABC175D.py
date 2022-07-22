N, K = map(int, input().split())
P = list(map(int, input().split()))
P = [p - 1 for p in P]
C = list(map(int, input().split()))

INF = 10**18
ret = -INF

for i in range(N):
    v = i
    cycle_sum = 0
    cycle_count = 0
    while True:
        cycle_count += 1
        cycle_sum += C[v]
        v = P[v]
        if v == i:
            break
    path = 0
    cnt = 0
    while True:
        cnt += 1
        path += C[v]
        if cnt > K:
            break
        num = (K - cnt) // cycle_count
        score = path + max(0, cycle_sum) * num
        ret = max(ret, score)
        v = P[v]
        if v == i:
            break

print(ret)

"""
間違っている
そもそもDではダブリングでないのでは？

ループとそれ以外で管理して全探索するイメージ

"""
