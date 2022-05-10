N, K = map(int, input().split())
A = list(map(int, input().split()))
ret = 0
for a in A:
    ret += a * (a + 1) // 2
if ret <= K:
    print(ret)
    exit()

A.sort()
f = A.pop()
c = 1

ret = 0
while len(A):
    nxt = A.pop()
    if c * (f - nxt) >= K:
        break
    else:
        ret += c * (f * (f + 1) // 2 - nxt * (nxt + 1) // 2)
        K -= c * (f - nxt)
        c += 1
        f = nxt

if K != 0:
    d = f - K // c
    e = c - K % c
    r = c * (f * (f + 1) // 2 - d * (d + 1) // 2) + d * e
    ret += r

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

"""
