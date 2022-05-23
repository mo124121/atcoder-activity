C = input()

if C == "a" or C == "z" * 20:
    print("NO")
elif len(C) == 1:
    print(chr(ord(C) - 1) + "a")
elif C == "z" and C == C[0] * len(C):
    print(C[:-1] + chr(ord(C[-1]) - 1) + "a")
elif C != C[::-1]:
    print(C[::-1])
else:
    ord_a = ord("a")
    C_v = list(map(lambda x: ord(x) - ord_a + 1, C))
    C_sum = sum(C_v)
    ret = (C_sum // 26) * "z"
    if C_sum % 26 != 0:
        ret += chr(C_sum % 26 + ord_a - 1)
    print(ret)


"""
パターン分けの嵐

NO
a
z*20

1文字

zで同一

それ以外

"""
