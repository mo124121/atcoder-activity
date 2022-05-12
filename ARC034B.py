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
    f_max = len(str(N)) * 9
    ans = []
    for i in range(max(0, N - f_max), N + 1):
        if f(i) == N:
            ans.append(i)
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
