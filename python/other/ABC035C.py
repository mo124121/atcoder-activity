N, Q = map(int, input().split())
ban = [0] * N
for i in range(Q):
    l, r = map(int, input().split())
    ban[l - 1] += 1
    if r != N:
        ban[r] -= 1
for i in range(N - 1):
    ban[i + 1] += ban[i]

ret = []
for b in ban:
    ret.append(b % 2)

print(*ret, sep="")
