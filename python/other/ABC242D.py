from collections import Counter


S = input()
Q = int(input())
ret = []
for i in range(Q):
    t, k = map(int, input().split())
    base_k = (k - 1) >> t
    shift2 = 0
    if base_k > 0:
        shift2 = 1 << t
    shift = t + Counter(bin(k - 1 - base_k * shift2)[2:])["1"]
    r = chr((ord(S[base_k]) - ord("A") + shift) % 3 + ord("A"))
    ret.append(r)
print(*ret, sep="\n")
