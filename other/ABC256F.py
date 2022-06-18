N, Q = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353

AA = [0] * N
AA[0] = 1
B = [0] * N
C = [0] * N
D = [0] * N
B[0] = C[0] = D[0] = A[0]

for i in range(N - 1):
    B[i + 1] = (B[i] + AA[i + 1]) % MOD
    C[i + 1] = (C[i] + B[i + 1]) % MOD
    D[i + 1] = (D[i] + C[i + 1]) % MOD

print(*A)
print(*B)
print(*C)
print(*D)
