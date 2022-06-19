N, K = map(int, input().split())
S = str(K)
if K>int(S[::-1]):
    print(0)
    exit()
if K==int(S[::-1]):
    mirror=True
else:
    mirror=False
ret = 0
i = 0
flag = True
while flag:
    if int(S + "0" * i) <= N:
        ret += 1
    else:
        flag = False
    if not mirror:
        if int(S[::-1] + "0" * i) <= N:
            ret += 1
        else:
            flag = False
    i += 1
print(ret)
