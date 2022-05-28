N = int(input())
A = [0] + list(map(int, input().split())) + [10**10]

gradients = [A[i + 1] - A[i] for i in range(N + 1)]
slopes_signs = []
for i, g in enumerate(gradients):
    if g != 0:
        slopes_signs.append((i, g > 0))
ret = [0] * N

for i in range(len(slopes_signs) - 1):
    j1, f1 = slopes_signs[i]
    j2, f2 = slopes_signs[i + 1]
    if f1 ^ f2:
        ret[j1] = 1


print(*ret)


"""
株の売買問題

上げる時、下げるときをトリガに換金する
問題は最後

同じ時どうする？
経路圧縮しとくのが楽？

解説が天才すぎる

"""
