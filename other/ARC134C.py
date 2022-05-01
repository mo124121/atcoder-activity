def comb(n, r, MOD):
    r = min(r, n - r)
    if n == 0:
        return 1
    big = 1
    small = 1
    for i in range(1, r + 1):
        big *= n + 1 - i
        small *= i
    return big // small % MOD


N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353

A[0] -= K
if A[0] < 0:
    print(0)
    exit()
ret = 1
for ai in A[1:]:
    if A[0] < ai:
        ret = 0
        break
    ret *= comb(ai + K - 1, K - 1, MOD)
    ret %= MOD
    A[0] -= ai

if A[0] > 0:
    ret *= comb(A[0] + K - 1, K - 1, MOD)
    ret %= MOD

print(ret)


"""
やってるやつ
やり方わすれているやつ


最低限出来るセットを箱ごとに作り、
あと自由な分数えるイメージ

112 1
1 112

まず、条件を満たすために1個を各箱にいれる　これは1パターンしかない
次に1以外の数を1とペアとして各箱に入れる この時点で1が足りなくなったら0
最後にのこった1を入れる


"""
