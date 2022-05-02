S = input().replace("25", "A")

ret = 0
count = 0
for c in S:
    if c == "A":
        count += 1
    else:
        ret += count * (count + 1) // 2
        count = 0

ret += count * (count + 1) // 2
print(ret)
