class FenwickTree:
    def __init__(self, n, init_data=0):
        self.size = n
        self.tree = [0] * (n + 1)
        if init_data != 0:
            for i in range(1, n + 1):
                self.add(i, init_data)

    def sum(self, i):
        ret = 0
        i += 1
        while i > 0:
            ret += self.tree[i]
            i -= i & -i
        return ret

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def get(self, i):
        return self.sum(i) - self.sum(i - 1)

    def lower_bound(self, w):
        if w <= 0:
            return 0
        x = 0
        r = 1
        while r < self.size:
            r = r << 1
        length = r
        S = 0
        while length > 0:
            if length + x < self.size and self.tree[x + length] < w:
                w -= self.tree[x + length]
                x += length
            length = length >> 1
        return x

    def show(self):
        ret = []
        for i in range(self.size):
            ret.append(self.get(i))
        print(*ret)


N = int(input())
C = list(map(int, input().split()))
X = list(map(int, input().split()))
A = [[] for _ in range(N + 1)]
for i in range(N):
    x = X[i]
    A[0].append(x)
    A[C[i]].append(x)

ret = 0
ft = FenwickTree(N + 1)
for a in A[0]:
    ret += ft.sum(N) - ft.sum(a)
    ft.add(a, 1)
for a in A[0]:
    ft.add(a, -1)


for i in range(1, N + 1):
    m = len(A[i])
    for a in A[i]:
        ret -= ft.sum(N) - ft.sum(a)
        ft.add(a, 1)
    for a in A[i]:
        ft.add(a, -1)

print(ret)


"""
非減少なので同じでも大丈夫

コストのあるソート設計
どれだけコストのかかるスワップをなくせるか？

操作はバブルソート的

なんとなく、同じ色の中で固まっている間にソートするのがよさそう

上界を考える？
同じ色じゃないところまで移動させる操作はコストになりそう
そんなに自明ではないのかも

希望の位置と自分の位置までにある他の色の個数とか？その合計？の半分?スワップするので

逆に自分と同じ色の個数を数えるとか？


ソート前とソート後の位置と関係は出せる
その間の自分の色と同じ色の個数は出せるか？


ソート後の位置ベースで、
自分の進む方向に自分より大きいものが移動の前後で存在するか？
カウント使えば行けるのでは？無理？bisect使う？


"""
