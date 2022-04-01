N = int(input())
i = 2
prime_factors = dict()
div_sum = 1
n = N
while i * i <= N:
    while n % i == 0:
        n = n // i
        if i in prime_factors:
            prime_factors[i] += 1
        else:
            prime_factors[i] = 1
    i += 1
if n != 1:
    prime_factors[n] = 1

ret = 0
for v in prime_factors.values():
    i = 0
    while v > 0:
        i += 1
        v -= i
    if v < 0:
        i -= 1
    ret += i

print(ret)
