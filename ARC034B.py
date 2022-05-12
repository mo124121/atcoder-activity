def f(x):
    ret = 0
    for c in str(x):
        ret += int(c)
    return ret + x


def greed(N):
    R = []
    for x in range(1, N + 1):
        if N == f(x):
            R.append(x)
    return R


def solve(N):

    ans = []

    def rec(N, x, keta):
        if keta == 1:
            y = f(x)
            if (N - y) >= 0 and (N - y) % 2 == 0:
                ans.append(x + (N - y) // 2)
            return

        for i in range(9, -1, -1):
            xi = x + i * 10 ** (keta - 1)
            yi = f(xi)
            v_max = 10 ** (keta - 1) - 1 + 9 * (keta - 1) * keta // 2
            if N < yi:
                continue
            if N > yi + v_max:
                break
            rec(N, xi, keta - 1)

    rec(N, 0, len(str(N)))
    ans.sort()

    return ans


def submit():
    N = int(input())
    ans = solve(N)
    print(len(ans))
    if len(ans) != 0:
        print(*ans, sep="\n")


submit()

# for debug
test = [i for i in range(1, 1001)]
# test = [119]

for t in test:
    g = greed(t)
    s = solve(t)
    if g != s:
        print(t, g, s)
        break

"""
N<10**18
上位桁の数字の中で達成可能なのを探していく
最大値でもたどり着かなければ打ち切る

たぶん再帰

テストによってACよし
なお解説ははるかにシンプルな模様

"""
