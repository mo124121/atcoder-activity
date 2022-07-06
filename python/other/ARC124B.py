N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()

x_cans = [A[0] ^ B[i] for i in range(N)]
C = [0] * N
ret = []
for i in range(N):
    t = x_cans[i]
    for j in range(N):
        C[j] = t ^ A[j]
    C.sort()
    if B == C:
        ret.append(t)

ret = list(set(ret))
ret.sort()
print(len(ret))
for r in ret:
    print(r)


"""
考察

XORコワイ

N<2000
N^2ぐらいはできる

いったんa x bの組み合わせを全てすればいいのでは？
その後順番にあるかチェックしていく

N*N + N*Nでできそう

ただ、同じaに対して複数あるケースが厄介
スタックにぶち込んで後で判断とか？

そも、XORならaが違えばxも違うのでは？

解説閲覧後
華麗すぎる、XOR履修したい

"""
