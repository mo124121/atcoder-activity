def tousa_sum(a, d, n):
    # 初項a,交差d,項数n
    return n * (2 * a + (n - 1) * d) // 2


N, K = map(int, input().split())
A = list(map(int, input().split()))
ret = 0
for a in A:
    ret += tousa_sum(1, 1, a)
if sum(A) <= K:
    print(ret)
    exit()
A.sort(reverse=True)
A.append(0)
ret = 0
for i in range(N):
    diff = A[i] - A[i + 1]
    cnt = diff * (i + 1)
    if cnt <= K:
        K -= cnt
        ret += tousa_sum(A[i], -1, diff) * (i + 1)
    else:
        d = K // (i + 1)
        m = K % (i + 1)
        ret += tousa_sum(A[i], -1, d) * (i + 1)
        ret += (A[i] - d) * m
        break

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

数字が合わないので解説見る
方針は間違ってないがバグらせとる

なるべく関数に任せる
踏査数列の和を使う

"""
