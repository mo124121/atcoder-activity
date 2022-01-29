N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

# 左と右で分けてN内で自分より小さい個数をカウント
left_count = 0
right_count = 0
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            left_count += 1
    for j in range(i + 1, N):
        if A[i] > A[j]:
            right_count += 1

# 左と右を場合分けして足しこむ
hoge_right = (K * (K + 1) // 2) % MOD
hoge_left = (K * (K - 1) // 2) % MOD
ret = (left_count * hoge_left + right_count * hoge_right) % MOD


print(ret)
