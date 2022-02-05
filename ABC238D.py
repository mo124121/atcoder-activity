from re import S


T = int(input())
a = [0] * T
s = [0] * S

ret = []
for i in range(T):
    a, s = map(int, input().split())
    r = s - a
    if r >= 0 and (r & a) == a:
        ret.append("Yes")
    else:
        ret.append("No")

print(*ret, sep="\n")
