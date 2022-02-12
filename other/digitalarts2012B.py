c = input()

if c == "a" or c == "z" * 20:
    print("NO")
    exit()

ret = ""
# 1文字
if len(c) == 1:
    ret = chr(ord("a") + 20 - 1) * ((ord(c) - ord("a") + 1) // 20) + "a" * (
        (ord(c) - ord("a") + 1) % 20
    )
# aのみ
elif c == "a" * len(c):
    ret = chr(ord("a") + len(c) - 1)
# zのみ
elif c == "z" * len(c):
    ret = c[:-1] + "ya"
# 全部同じ
elif c == c[0] * len(c):
    ret = c[:-2] + chr(ord(c[-2]) + 1) + chr(ord(c[-1]) - 1)
# 反転して同じじゃない
elif c != c[::1]:
    ret = c[::1]
else:
    ret = "".join(sorted(c))

print(ret)
