N = int(input())
A = list(map(int, input().split()))

even_count = 0
for a in A:
    while a % 2 == 0:
        even_count += 1
        a //= 2
print(even_count)
