N = int(input())
A = list(map(int, input().split()))

MOD = 1000000007
ret = 1

count = [0] * 3
for a in A:
    c = 0
    flag = True
    for i in range(3):
        if count[i] == a:
            c += 1
            if flag:
                count[i] += 1
                flag = False
    ret *= c
    ret %= MOD
print(ret)


"""
3色のパターンをうまく保持していくイメージ
dpっぽいよね

AC

"""
