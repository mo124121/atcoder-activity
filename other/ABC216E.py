def calc_sum(x):
    return x * (x + 1) // 2


N, K = map(int, input().split())
A = list(map(int, input().split()))
ret = 0
for a in A:
    ret += calc_sum(a)
if sum(A) <= K:
    print(ret)
    exit()
K -= sum(A)
A.sort(reversed=True)
pre = 0
for i, a in enumerate(A):
    if K + (N - i) * (a - pre) >= 0:
        ret -= (N - i) * (calc_sum(a) - calc_sum(pre))
        K += (N - i) * (a - pre)
    else:
        c = (-K - (N - i) * pre) // (N - i)
        d = -K % (N - i)
        ret -= (N - i) * (calc_sum(c) - calc_sum(pre))
        ret -= c * d
        break
    pre = a
print(ret)
"""
貪欲にやるなら、2番目に高いものまで眺めて、
1番目を2番目を下回るまで乗る・減らす

K<10**9なのでそのままやると間に合わない

同じ数字のアトラクション数をまとめる
最大だけでもいい

最大の楽しさを持つアトラクションに基本乗る、
2番目の楽しさまで
同じのが増えたら最大の楽しさを持つアトラクションが増える

結構WA
どうするか？

いっそ総合計を出してから引いていく

"""
