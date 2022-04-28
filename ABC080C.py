N = int(input())
F = []
for i in range(N):
    tmp = list(map(int, input().split()))
    f = 0
    for j, t in enumerate(tmp):
        f += t << j
    F.append(f)
P = [list(map(int, input().split())) for _ in range(N)]

ret = -(10**18)

for pat in range(1, 1024):
    r = 0
    for i in range(N):
        common = pat & F[i]
        count = 0
        for j in range(10):
            count += int((common >> j) & 1)
        r += P[i][count]
    ret = max(ret, r)
print(ret)

"""
問題がややこしい

10個の時間帯がある　これはいい

ほかのお店がN店舗ある

ほかのお店が10個の時間帯に開店しているかは与えられる

ほかのお店と被っている時間帯の個数毎に利益が決まっている

N<100

大した数字でもないので、
たぶんbit全探索でいい
2^10 =1024

"""
