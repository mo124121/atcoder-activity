N = 10**5 + 1

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False
i = 2
while i**2 <= N:
    if is_prime[i]:
        j = i * 2
        while j <= N:
            is_prime[j] = False
            j += i
    i += 1

commu = [0] * (10**5 + 1)

for i in range(1, 10**5 + 1):
    commu[i] = commu[i - 1]
    if is_prime[i] and i % 2 == 1 and is_prime[(i + 1) // 2]:
        commu[i] += 1

Q = int(input())
ret = []
for _ in range(Q):
    L, R = map(int, input().split())
    r = commu[R] - commu[L - 1]
    ret.append(r)

print(*ret, sep="\n")
