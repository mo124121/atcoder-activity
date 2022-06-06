N, M = map(int, input().split())

AB = []
for i in range(M):
    ab = list(map(int, input().split()))
    ab.sort()
    AB.append(ab)
AB.sort()

count = [0] * (N + 1)

for a, b in AB:
    count[a] += 1
    count[b] += 1

for c in count:
    if c % 2 == 1:
        print("NO")
        exit()

print("YES")
