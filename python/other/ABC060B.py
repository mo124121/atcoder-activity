A, B, C = map(int, input().split())

v = A % B
seen = set()
while v not in seen:
    seen.add(v)
    if v == C:
        print("YES")
        exit()
    v = (v + A) % B

print("NO")
