N = int(input())

for i in range(1, 50000):
    if i * 108 // 100 == N:
        print(i)
        exit()
print(":(")
