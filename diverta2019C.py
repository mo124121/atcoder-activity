N = int(input())
S = [input() for _ in range(N)]
summary = []
ret = 0
ab = 0
a = 0
b = 0
for s in S:
    ret += s.count("AB")
    if s[0] == "B" and s[-1] == "A":
        ab += 1
    elif s[0] == "B" and s[-1] != "A":
        b += 1
    elif s[0] != "B" and s[-1] == "A":
        a += 1

while True:
    if a > 0 and ab > 0:
        c = min(a, ab)
        ret += c
        ab -= c
    elif b > 0 and ab > 0:
        c = min(b, ab)
        ret += c
        ab -= c
    elif a > 0 and b > 0:
        c = min(a, b)
        ret += c
        a -= c
        b -= c
    elif ab > 2:
        ret += ab - 1
        ab -= ab
    else:
        break

print(ret)
