n, m, d = map(int, input().split())

ways = 0
if d == 0:
    ways = n
else:
    ways = 2 * (n - d)
ratio = ways / (n) / n
ret = ratio * (m - 1)

print(f"{ret:.7f}")


"""
平均　あるいは期待値

数が増える事での独立性をうまく活用する

"""
