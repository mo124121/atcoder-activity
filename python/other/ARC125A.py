N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

for c in set(T):
    if c not in S:
        print(-1)
        exit()

origin = S[0]
rev = 1 - S[0]
if rev in S:
    rev_i_r = S.index(rev)
    rev_i_l = list(reversed(S)).index(rev) + 1
else:
    print(len(T))
    exit()


moved = False

prev = origin
ret = 0
for t in T:
    if t != prev:
        if moved:
            ret += 1
        else:
            ret += min(rev_i_r, rev_i_l)
            moved = True
    ret += 1
    prev = t
print(ret)
