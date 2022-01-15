N = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
A, B, C = coins[0], coins[1], coins[2]
ret = 10000
for i in range(N // A + 1):
    target_a = N - i * A
    for j in range(N // B + 1 - i):
        target = target_a - j * B
        if target < 0:
            break
        if target % C == 0:
            ret = min(ret, i + j + target // C)
print(ret)
