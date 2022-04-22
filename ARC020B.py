n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]

ret = c * n
color = [0] * 2
for i in range(1, 11):
    for j in range(1, 11):
        if i == j:
            continue
        r = 0
        color[0] = i
        color[1] = j
        for k in range(n):
            r += int(a[k] != color[k % 2])
        ret = min(ret, r)
print(ret * c)
"""
n<10**2小さめ

ごり押しでいったらいい気はする
色数M
M*(M-1)*2のパターンで試して、差異の個数が最も小さくなるケース×cが答え

"""
