N = int(input())
A = list(map(int, input().split()))

tot = 0
count = 0
for a in A:
    if a > 0:
        tot += a
        count += 1

print((tot + count - 1) // count)
