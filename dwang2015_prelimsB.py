S = input()
S = S.replace("25", "A")

A_count = 0
ret = 0
for c in S:
    if c == "A":
        A_count += 1
    elif A_count > 0:
        ret += (A_count + 1) * A_count // 2
        A_count = 0
ret += (A_count + 1) * A_count // 2
print(ret)

"""
この手の奴はreplaceが便利
"""
