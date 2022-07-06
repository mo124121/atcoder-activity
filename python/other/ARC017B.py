N, K = map(int, input().split())
A = [0] * N
for i in range(N):
    A[i] = int(input())

B = [0] * N
for i in range(N - 1):
    B[i + 1] = B[i] + int(A[i + 1] > A[i])

ret = 0
for i in range(N - K + 1):
    ret += int(B[i + K - 1] - B[i] == K - 1)
print(ret)

"""
最長増加部分列っぽくはある
よく読むと連続の区間なので違う

大事なのは増減だけなので、
いったん増加しているかどうかの0,1に変換してもよい

上記配列の累積和をとって区間の和が
配列長さに一致すればよい

解説後
連続する部分列を探し、
その部分列でシフトできる量を足し合わせていく

"""
