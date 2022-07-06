ret = 0
for _ in range(3):
    s, e = map(int, input().split())
    ret += s * e
print(ret // 10)
