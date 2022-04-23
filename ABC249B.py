S = input()

SMALL = [chr(ord("a") + i) for i in range(26)]

seen = {}

flag_big = False
flag_small = False
flag_duplicated = False
for c in S:
    if c in seen:
        flag_duplicated = True
        break
    if c in SMALL:
        flag_small = True
    else:
        flag_big = True
    seen[c] = True

if flag_duplicated:
    print("No")
else:
    if flag_small and flag_big:
        print("Yes")
    else:
        print("No")
