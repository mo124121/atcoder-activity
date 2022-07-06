S = input()
V = S.split("+")
ret = 0
for v in V:
    if len(v) == 1:
        if int(v) != 0:
            ret += 1
    else:
        if "0" not in v:
            ret += 1

print(ret)

"""
+で区切られた要素毎に0が含まれるかどうか
"""
