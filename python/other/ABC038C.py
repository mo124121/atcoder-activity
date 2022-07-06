N = int(input())
A = list(map(int, input().split()))
ret = 0
l = 0
r = 1

while l < N:
    while r < N and A[r - 1] < A[r]:
        r += 1
    d = r - l
    ret += d * (d + 1) // 2
    l = r
    r = l + 1

print(ret)


"""
N<10**5
連続増加部分を探す
逆に言うと切れたら仕切り直し
とすると各連続増加部分を見つけて、
その部分内に存在するパターンを数え上げればいい
dC2とかそんなんd(d-1)//2
違ってた

Σd=d(d+1)//2

解説後
rの内部ループで伸びるごとに数え上げてもいい

"""
