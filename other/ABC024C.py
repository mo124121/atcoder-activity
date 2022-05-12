N, D, K = map(int, input().split())
L = [0] * D
R = [0] * D
for i in range(D):
    L[i], R[i] = map(int, input().split())
S = [0] * K
T = [0] * K
for i in range(K):
    S[i], T[i] = map(int, input().split())

ret = [D] * K

for i, (l, r) in enumerate(zip(L, R)):
    for k in range(K):
        if S[k] < T[k]:
            if l <= S[k] <= r:
                S[k] = min(r, T[k])
        elif S[k] > T[k]:
            if r >= S[k] >= l:
                S[k] = max(l, T[k])
        elif S[k] == T[k] and ret[k] == D:
            ret[k] = i
print(*ret, sep="\n")


"""
基本的に貪欲でいいように見える
各日、行けるだけ行く
"""
