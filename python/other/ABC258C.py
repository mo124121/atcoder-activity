N, Q = map(int, input().split())
S = input()
cur = 0

ret = []
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        cur -= x
    else:
        ret.append(S[(cur + x - 1) % N])

print(*ret, sep="\n")
