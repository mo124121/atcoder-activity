N = int(input())
i = 2
primes = dict()
n = N
while i * i <= N:
    while n % i == 0:
        n = n // i
        if i in primes:
            primes[i] += 1
        else:
            primes[i] = 1
    i += 1
if n != 1:
    primes[n] = 1
primes[1] = 1


def order_count(n):
    i = 1
    while 10**i <= n:
        i += 1
    return i


ret = 10
cans = set((1,))
for p, c in primes.items():
    tmp = set()
    for can in cans:
        for i in range(1, c + 1):
            a = can * p**i
            b = N // a
            a_order = order_count(a)
            b_order = order_count(b)
            ret = min(ret, max(a_order, b_order))
            if a < b:
                tmp.add(a)
            else:
                break
    cans = cans.union(tmp)

print(ret)


"""
とりあえず素因数分解
それぞれをAとBに振り分けて、
最大桁が小さくなるように割り振る

10**10
大きい、O(N)でもだめ
logNでできる方法を探す必要がある
sqrt(N)ぐらいな感じする

最も因数が多くなるのは？
2だけで構成されてるとき、2^34ぐらい？
とすると、高々それぐらいの因数しか存在しない

さすがにbit全探索するにはおおきい

ただ、どっかでかけても改善しなくなるので枝切りしていい
基準は>10**6
34* 10**6まで最大検証すればいい、勝った

はい1WA
1の時の考慮が抜けていた、最小値ぐらいは試すべき


"""
