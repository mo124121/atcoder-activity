S = input()
K = int(input())

D = 5000 * ((10**4) ** 3)

n = 0
i1 = len(S)
for i, s in enumerate(S):
    if s != "1":
        i1 = i
        n = int(s)
        break

if K <= i1:
    print(1)
else:
    print(n)
