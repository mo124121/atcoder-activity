X = int(input())

if X > 10000:
    print(1)
    exit()

n_max = X // 100


ret = 0
for i in range(n_max + 1):
    for j in range(n_max + 1 - i):
        for k in range(n_max + 1 - i - j):
            for l in range(n_max + 1 - i - j - k):
                for m in range(n_max + 1 - i - j - k - l):
                    if (X - i * 100 - j * 101 - k * 102 - l * 103 - m * 104) % 105 == 0:
                        ret = 1

print(ret)
