A, B, K = map(int, input().split())


class Binominal:
    def __init__(self, N):
        c = [[0] * (N + 1) for _ in range(N + 1)]

        c[0][0] = 1
        for i in range(N):
            for j in range(i + 1):
                c[i + 1][j] += c[i][j]
                c[i + 1][j + 1] += c[i][j]
        self.c = c

    def calc(self, n, r):
        if r < 0 or n < r:
            return 0
        return self.c[n][r]


bn = Binominal(A + B)
ret = []
while A > 0 and B > 0:
    v = bn.calc(A + B - 1, A - 1)
    if K <= v:
        ret.append("a")
        A -= 1
    else:
        ret.append("b")
        B -= 1
        K -= v
ret += ["a"] * A + ["b"] * B

print("".join(ret))


"""
再帰を使うイメージ
aabbbbb
baabbbb
bbaabbb
bbbaabb
bbbbaab
bbbbbaa

aaabbbbb
baaabbbb

考えてたらbit使うほうがいい気がしてきた

頭がフットーしそうなので解説動画見る

2項係数引っ張ってきて引くのが楽そう

辞書順は上の文字から決めていくといい
二項係数を事前計算して当てはめていく

"""
