S = input()
ret = 0
prev = S[0]
for c in S[1:]:
    if c != prev:
        ret += 1
    prev = c
print(ret)
