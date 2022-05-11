N = int(input())


def f(x):
    ret = 0
    for c in str(x):
        ret += int(c)
    return ret + x


def greed(N):
    ret = 0
    R = []
    for x in range(1, N + 1):
        if N == f(x):
            ret += 1
            R.append(x)
    print(ret)
    print(*R)


greed(N)

ans = []


def rec(N, x, keta):
    if keta == 1:
        x *= 10
        y = f(x)
        if (N - y) % 2 == 0:
            ans.append(x + (N - y) // 2)
        return

    for i in range(9, -1, -1):
        xi = x * 10**keta + i + i * 10 ** (keta - 1)
        v_max = 10 ** (keta - 1) - 1 + 9 * (keta - 1) * (keta - 2) // 2
        if N < xi:
            continue
        if N > xi + v_max:
            break
        rec(N, x * 10 + i, keta - 1)


rec(N, 0, len(str(N)))
ans.sort()
print(len(ans))
print(*ans)

"""
N<10**18
上位桁の数字の中で達成可能なのを探していく
最大値でもたどり着かなければ打ち切る

たぶん再帰

"""
