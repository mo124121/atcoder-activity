H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

q = []
q.append((0, 0))
A[0][0] = "."

while len(q):
    x, y = q.pop()
    if (x, y) == (W - 1, H - 1):
        break
    if x + 1 < H and A[x + 1][y] == "#":
        q.append((x + 1, y))
        A[x + 1][y] = "."
    elif y + 1 < W and A[x][y + 1] == "#":
        q.append((x, y + 1))
        A[x][y + 1] = "."


for h in range(H):
    for w in range(W):
        if A[h][w] == "#":
            print("Impossible")
            exit()
print("Possible")


"""
要は軌跡が描かれている
右下に行くだけなら、1本道
余計なことをしてたら増えている
通ったところを消していって、それでも残っていたらNGにする
行き止まりみたいなことがあったら引き返しているのでNG

とすると適当に移動して
-右下に移動できて
-通ってないマスがないという状態

"""
