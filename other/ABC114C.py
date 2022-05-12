from collections import Counter


def check(x):
    count = Counter(str(x))
    if len(count) == 3 and count["7"] > 0 and count["5"] > 0 and count["3"] > 0:
        return True
    return False


def greed(N):
    ret = []
    for i in range(N + 1):
        if check(i):
            ret.append(i)
    return ret


def solve(N):
    v = [3, 5, 7]
    keta = len(str(N))
    ret = []
    for dgt in range(3, keta + 1):
        ma = 3**dgt
        for msk in range(ma):
            x = 0
            m = msk
            cn = [0] * 3
            for _ in range(dgt):
                d = m % 3
                x = x * 10 + v[d]
                m //= 3
            if x <= N and check(x):
                ret.append(x)
    return ret


def submit():
    N = int(input())
    print(len(solve(N)))


submit()

ts = [i + 1 for i in range(1000)]
for t in ts:
    r1 = sorted(greed(t))
    r2 = sorted(solve(t))
    if r1 != r2:
        print(t, r1, r2)
        exit()

"""
桁のコントロール難しい、苦手
3つ選んだ上で、残りの桁は0124689

上の桁から落としていく感じ
再帰で考える感じ

そもそも7 5 3 しかでない問題　誤読
"""
