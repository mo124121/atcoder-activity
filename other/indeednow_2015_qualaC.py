N = int(input())
S = [int(input()) for _ in range(N)]
Q = int(input())
K = [int(input()) for _ in range(Q)]

S.sort(reverse=True)

for k in K:
    if k >= N or S[k] == 0:
        print(0)
    else:
        print(S[k] + 1)

"""
二分探索っぽいが、普通に点数でソートして、許容できる点数を決めればいいのでは？

ACだが、もう少しコーナーケースに対する挙動を検討すべき

"""
