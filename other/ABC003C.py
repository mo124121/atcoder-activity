N, K = map(int, input().split())
R = list(map(int, input().split()))
R.sort()

ret = 0

for i in range(N - K, N):
    ret = (ret + R[i]) / 2
print("{:.7f}".format(ret))


"""
たぶん小さいほうから足していくほうがゲインが大きい
ソートして足してく

"""
