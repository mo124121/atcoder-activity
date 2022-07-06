N = int(input())
A = list(map(int, input().split()))
A.sort()
seen = set()

for a in A:
    shift = 0
    while (a >> shift) & 1 ^ 1:
        shift += 1
    seen.add(a >> shift)
print(len(seen))
