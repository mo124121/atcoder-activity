N = int(input())
A = list(map(int, input().split()))

memo_min = [0] * (N + 1)
memo_max = [0] * (N + 1)
memo_min[-1] = A[-1]
memo_max[-1] = A[-1]
for i in range(N - 1, -1, -1):
    a = A[i]
    memo_min[i] = (memo_min[i + 1] + 1) // 2 + a
    memo_max[i] = memo_max[i + 1] + a

ret = 0
x = 1

for i in range(N + 1):
    if memo_min[i] <= x:
        x = min(x, memo_max[i])
        ret += x
        x -= A[i]
        x *= 2
    else:
        print(-1)
        exit()

print(ret)

"""
解説AC

・各層でとれる範囲を考える
・2回の走査を考える
"""
