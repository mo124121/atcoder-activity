N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
seen_b = set()
b_sizes = []
for b in B:
    seen_b.add(b)
    b_sizes.append(len(seen_b))
l_a = 0
l_b = -1
seen_a = set()
seen_b = set()
a_not_b = set()
b_not_a = set()
ok = {}
while l_a < N:
    a = A[l_a]
    seen_a.add(a)
    if a not in seen_b:
        a_not_b.add(a)

    while len(a_not_b):
        l_b += 1
        if l_b == N:
            break
        b = B[l_b]
        seen_b.add(b)
        if b in a_not_b:
            a_not_b.discard(b)
    r_b = l_b
    while r_b < N:
        if B[r_b] not in seen_b:
            break
        r_b += 1

    r_a = l_a
    while r_a < N:
        if A[r_a] not in seen_a:
            break
        ok[r_a] = (l_b, r_b)
        r_a += 1
    l_a = r_a + 1
    l_b = r_b + 1

Q = int(input())
ret = []
for i in range(Q):
    x, y = map(int, input().split())
    if x not in ok:
        ret.append("No")
        continue
    l, r = ok[x]
    if l <= y < r:
        ret.append("Yes")
    else:
        ret.append("No")

print(*ret, sep="\n")
