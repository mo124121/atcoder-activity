N = int(input())
i = 2
prime_c = dict()
n = N
while i * i <= N:
    while n % i == 0:
        n = n // i
        if i in prime_c:
            prime_c[i] += 1
        else:
            prime_c[i] = 1
    i += 1
if n != 1:
    prime_c[n] = 1

ret = 1
for i, count in prime_c.items():
    r = 0
    for j in range(count + 1):
        r += i**j
    ret *= r

if ret > 2 * N:
    print("Abundant")
elif ret < 2 * N:
    print("Deficient")
else:
    print("Perfect")

"""
完全数に関する知識がいりそう

N<10**10

とりあえず約数列挙する？

一定以上になるとあっという間に超えそうな気がする

ただ約数の個数はあっという間に爆発するはず
Π(素因数の出現数+1)
のパターン
ΠΣr^i
みたいな感じか

AC

解説後
素因数分解せずとも、i**2<=Nの範囲で
割り切れるかどうか判定して、わる数と商をそれぞれかければよい
"""
