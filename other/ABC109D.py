H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

N = 0
ret = []
for h in range(H):
    for w in range(W - 1):
        if A[h][w] % 2 == 1:
            A[h][w] -= 1
            A[h][w + 1] += 1
            ret.append((h + 1, w + 1, h + 1, w + 2))
for h in range(H - 1):
    if A[h][W - 1] % 2 == 1:
        A[h][W - 1] -= 1
        A[h + 1][W - 1] += 1
        ret.append((h + 1, W, h + 2, W))

print(len(ret))
for r in ret:
    print(*r)

# print("After")
# for a in A:
#     print(*a)


"""
貪欲でいいように見える
全体を走査していって、奇数の時に横に動かす

"""
