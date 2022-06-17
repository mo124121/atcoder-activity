N = int(input())
ret = []
v = 1
while N:
    if v & N:
        ret.append(v)
        N -= v
    v *= 2

print(len(ret))
for r in ret:
    print(r)
