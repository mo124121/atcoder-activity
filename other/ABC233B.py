L, R = map(int, input().split())
S = input()
L -= 1
R -= 1
s1 = S[:L]
s2 = "".join(list(reversed(S[L : R + 1])))
s3 = S[R + 1 :]
print(s1 + s2 + s3)
