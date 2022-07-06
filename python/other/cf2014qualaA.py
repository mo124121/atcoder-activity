A = int(input())

for i in range(1001):
    if i**3 == A:
        print("YES")
        exit()

print("NO")
