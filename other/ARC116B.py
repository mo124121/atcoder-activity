N = int(input())
A = list(map(int, input().split()))
A.sort()
MOD = 998244353
ret = 0

Aj = [0] * N

for i in range(1, N):
    Aj[i] = 2 * Aj[i - 1] + A[i - 1]
    Aj[i] %= MOD

for i in range(1, N):
    ret += A[i] * Aj[i]
    ret %= MOD

for a in A:
    ret += a**2
    ret %= MOD


print(ret)

"""
びっくりパターン数の総和

ソートしてある範囲のパターン数×範囲左端の数×範囲右端とか
それだとN**2選び方があるので間に合わない

事前に何らか計算できないか？
右に行くほどパターン数は倍になっていく-> 0x11111とかとかけてけばよくね？
あーでも係数がいる、どうする->bitシフトすれば足しなす必要はない
これは定数倍の効率化する発想

2 3 4

2 3*1 4*2
2*2 3*1 4
2*1 3


解説後

数式変形
"""
