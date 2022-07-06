N = int(input())
A = list(map(int, input().split()))
seen = set(A)

for i in range(2001):
    if i not in seen:
        print(i)
        exit()
