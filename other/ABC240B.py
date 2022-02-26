N = int(input())
A = list(map(int, input().split()))

count = {}
for a in A:
    count[a] = True

print(len(count))
