N = int(input())
A = list(map(int, input().split()))

count = [0] * (N + 1)

for a in A:
    count[a] += 1

print(count.index(3))
