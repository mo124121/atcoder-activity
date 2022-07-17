S = input()
N = len(S)
ret = 0
for i, s in enumerate(S):
    if s == "U":
        ret += 2 * i + (N - i - 1)
    else:
        ret += 2 * (N - i - 1) + i
print(ret)
