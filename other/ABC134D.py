N = int(input())
A = [0] + list(map(int, input().split()))

B = [0] * (N + 1)
for i in range(N, 0, -1):
    r = 0
    for j in reversed(range(2 * i, N + 1, i)):
        r += B[j]
    B[i] = (A[i] - r) % 2
ret = []
for i in range(N + 1):
    if B[i] != 0:
        ret.append(i)
print(len(ret))
if ret:
    print(*ret)

"""
日本語がわからん
mod計算っぽい


"""
