N, A, B = map(int, input().split())

S = [int(input()) for _ in range(N)]

Sx = max(S)
Sn = min(S)
Ss = sum(S)

if Sx == Sn:
    print(-1)
    exit()


p = B / (Sx - Sn)
q = A - p * Ss / N
print("{:0.7f} {:0.7f}".format(p, q))


"""
N<2*10**5

A'=ΣSi/N
↓
A=Σ(p*Si+q)/N
A=p*ΣSi/N + q
A=p*A'+q

B'=Sx-Sn
↓
B=p*Sx+q-p*Sy-q
B=p*(Sx-Sy)
p=B/(Sx-Sy)
p=B/B'

q=A-p*A'


あーpも負でいいのか、めんどくさい…
そうでもなかった
"""
