A = int(input())

for i in range(1, 1001):
    if A == i**3:
        print("YES")
        exit()

print("NO")
