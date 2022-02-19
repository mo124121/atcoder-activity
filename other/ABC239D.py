A, B, C, D = map(int, input().split())

Tak = "Takahashi"
Ao = "Aoki"

is_prime = [True] * 201
is_prime[0] = is_prime[1] = False
for i in range(2, 201):
    if is_prime[i]:
        q = i * 2
        while q < 201:
            is_prime[q] = False
            q += i
p = {}
for i in range(201):
    if is_prime[i]:
        p[i] = True

flag_tak = False

for i in range(A, B + 1):
    flag_tmp = True
    for j in range(C, D + 1):
        if i + j in p:
            flag_tmp = False
            break
    if flag_tmp:
        flag_tak = True
        break

if flag_tak:
    print(Tak)
else:
    print(Ao)
