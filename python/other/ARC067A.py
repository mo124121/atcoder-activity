N = int(input())
count = [0] * (N + 1)
MOD = 10**9 + 7
for j in range(2, N + 1):
    i = 2
    count_j = dict()
    n = j
    while i * i <= j:
        while n % i == 0:
            n = n // i
            if i in count_j:
                count_j[i] += 1
            else:
                count_j[i] = 1
        i += 1
    if n != 1:
        count_j[n] = 1
    for k, v in count_j.items():
        count[k] += v

ret = 1
for i in range(2, N + 1):
    ret = ret * (count[i] + 1) % MOD
print(ret)

"""
正の約数

N<10**3
そんなに大きくない

Nまでの数字それぞれの素因数を数えて、
Π素因数の数
あたりか？

"""
