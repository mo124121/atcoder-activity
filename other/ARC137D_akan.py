N, M = map(int, input().split())
A = list(map(int, input().split()))

ret = []
B = A[N - 1]
for i in range(N - 1):
    B ^= A[i]
ret.append(B)
for j in range(M - 1):
    ret.append(A[N - 1] - A[j % N])

print(*ret)

"""
1 A1
2 A21=A1
3 A31=A1
4 A41=A1
5 a51=a1

1 A2
2 A22=A2^A1
3 A32=A22^A1=A2^a1^a1=a2
4 A42=a32^a1=a2^a1
5 a52=a42^a41=a2^a1 ^ a1 =a2

1 A3
2 A23=a3^a2^a1
3 A33=a23^a22^a21=a3^a2^a1 ^ a2^a1 ^ a^1 =a3^a1
4 A43=a33^a32^a31=a3^a1 ^ a2 ^ a1 = a3^a2
5 a53=a43^a52=a3^a2 ^ a2=a3

1 A4
2 A24=a14^a23=a4^a3^a2^a1
3 A34=a24^a33=a4^a3^a2^a1 ^ a3^a1 = a4^a2
4 A44=a34^a43=a4^a2 ^ a3^a2 =a4^a3
5 A54=a44^a53=a4^a3 ^ a3 = a4



"""
