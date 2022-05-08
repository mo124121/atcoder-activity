from heapq import heappop, heappush


N = int(input())


def ok(N):
    base = [6, 10, 15]
    A = []
    for b in base:
        x = b
        while x < 10**4:
            A.append(x)
            x += b
    bad = [i * 30 for i in range(10**4 // 30 + 1)]
    A = list(set(A).difference(bad))
    A.sort()
    return A[:N]


A = ok(N)
print(*A)


def ng(N):
    B = [2, 3, 5]
    prod = 1
    for b in B:
        prod *= b
    A = []
    for b in B:
        A.append(prod // b)
    seen = set(A)
    x = A.copy()

    h = []
    for i in range(len(A)):
        heappush(h, (A[i], i))

    while len(A) < N:
        a, i = heappop(h)
        a += x[i]
        while a % B[i] == 0 or a in seen:
            a += x[i]
        seen.add(a)
        A.append(a)
        heappush(h, (a, i))
    print(*A)


# for debug
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


x = A[0]
for a in A:
    x = gcd(x, a)
print(x)

"""
最小公倍数を出すイメージ？

全体では最大公約数は1->互いに素なものが含まれる　1組以上
全ての組に関して、gcd>1 互いに素ではない
矛盾してない？

例題の約数列挙したらわかったが、
共有しない素数がそれぞれあるイメージ

とりあえず素数列を必要数生成して、
省く素数を1個ずつづらしていく

1万以下の制約
別に全部使う必要はない
2 3 5だけ使って、2だけ増やしていくとかでいい

あかんでかすぎる

×でなく足せば？

"""
