N, K = map(int, input().split())

if K > N // 2:
    print(-1)
    exit()

P = list(range(1, N + 1))

pos = 0
ret = []
while True:
    if N - pos - 4 * K < 0:
        break
    ret.extend(P[pos + K : pos + 2 * K] + P[pos : pos + K])
    pos += 2 * K

if N - pos < 3 * K:
    ret.extend(P[pos + K :] + P[pos : pos + K])
else:
    shift = N % K
    ret.extend(P[pos + K : pos + 2 * K])
    ret.extend(P[pos : pos + shift])
    ret.extend(P[N - K :])
    ret.extend(P[pos + shift : pos + K])
    ret.extend(P[pos + 2 * K : pos + 2 * K + shift])

print(*ret)
