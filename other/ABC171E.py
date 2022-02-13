N = int(input())
A = list(map(int, input().split()))

L = [A[0]]
R = [A[N - 1]]

for i in range(1, N - 1):
    L.append(L[-1] ^ A[i])
    R.append(R[-1] ^ A[-i - 1])

ret = [0] * N
ret[0] = R[-1]
ret[N - 1] = L[-1]

for i in range(1, N - 1):
    ret[i] = L[i - 1] ^ R[-i - 1]

print(*ret)
