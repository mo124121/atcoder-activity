N = input()

n = int(N)

for i in range(1, 100001):
    if int(str(i) * 2) > n:
        print(i - 1)
