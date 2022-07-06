class UnionFind:
    def __init__(self, N):

        self.parent = [0] * N
        for i in range(N):
            self.parent[i] = i

    def root(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return
        else:
            self.parent[root_x] = root_y

    def same(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        return root_x == root_y


N = int(input())
A = list(map(int, input().split()))
if N == 1:
    print(0)
    exit()


ret = 0
uf = UnionFind(2 * 10**5 + 1)

for i in range(N // 2 + 1):
    if not uf.same(A[i], A[-1 - i]):
        uf.unite(A[i], A[-1 - i])
        ret += 1

print(ret)

"""
愚直にやればいいように見える　一度同じになった数字は変更しようと同じなので回文から逸脱しない
両端から同一チェックをして違えば同じに…といいつつ、
どちらに合わせるか？の問題が残る

それもどっちでもいい？
サンプルで確認してみる

1 5 3 2 5 2 3 1
a 左から
1 5 5 2 5 2 5 1
1 5 5 5 5 5 5 1
b 右から
1 3 3 2 3 2 3 1
1 2 2 2 2 2 2 1

どっちでもいい気がする
これで変換する数字の個数が最小だったらあぶなかった

各整数の変換後辞書を持ちつつ、
左優先で書き換えていく感じで

あーufあったほうがいいかなあ
書き換え先は同じにしておきたい

"""
