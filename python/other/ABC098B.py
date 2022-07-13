N = int(input())
S = input()

ret = 0
for i in range(1, N - 1):
    ret = max(ret, len(set(S[:i]).intersection(set(S[i:]))))
print(ret)
