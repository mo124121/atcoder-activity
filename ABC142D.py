A, B = map(int, input().split())


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


C = gcd(A, B)
i = 2
primes = dict()
n = C
while i * i <= C:
    while n % i == 0:
        n = n // i
        if i in primes:
            primes[i] += 1
        else:
            primes[i] = 1
    i += 1
if n != 1:
    primes[n] = 1


print(len(primes) + 1)

"""
最大公約数を計算
因数分解して被らないように選べる数

選び方をどうするか？
2^a*3^b*5^c*7^d

素数ってどれくらいの密度で存在する？
logな感じだっけ？
とするとそんなに多くない？
10**5でも10**4あるわ…

4C0*4C1*(a+b+c+d)+4C1*3C1*(a(b+c+d)+b*(a+c+d)+c*(a+b+d)+d*(a+b+c))+...

とりあえず書いてみるか…
いやいや露骨に数が大きくなりすぎる

少し整理する
組み合わせを考える必要ななく、Π各素数の個数の取り合いでいいのではないか？
aを取り合う組み合わせ
|2 2 2 2 2
個数×AがとるかBがとるか


全部1はまずいので最後に引く？

考えすぎた、素数の数でいい

"""
