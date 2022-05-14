N = int(input())

is_primes = [True] * (N + 1)
is_primes[0] = is_primes[1] = False
i = 2
while i**2 <= N:
    if is_primes[i]:
        j = i * 2
        while j <= N:
            is_primes[j] = False
            j += i
    i += 1

if is_primes[N]:
    print("YES")
else:
    print("NO")
