N = int(input())
cs = [0] * (N)

for i in range(N):
    a = int(input())
    cs[i] = a
cs.sort(reverse=True)

if N == 1:
    if cs[0] % 2 == 0:
        print("second")
    else:
        print("first")
else:
    if cs[1] % 2 == 0:
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

再び考察


4WA/22
この時点でだいぶ答えは近いはず



"""
