N = int(input())
cs = [0] * (N)

for i in range(N):
    a = int(input())
    cs[i] = a
cs.sort()

turn = 0
count = 0
for i in range(N):
    b = cs[i] - count
    count += b
if count % 2 == 0:
    print("second")
else:
    print("first")


"""
考察
最初の考察を忘れてた、良くない
O(NlogN)
ソートはできる

たぶん手番管理を考えて再帰的にとくイメージ
ソートするのは正しい

たぶん食べれる最大が相手の手番の猶予をなくすのでベストなはず
1個だけ残して食べるのがたぶん

"""
