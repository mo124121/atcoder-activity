N = int(input())
ascent = True
prev = -1
ret = 0
count = 0
for _ in range(N):
    h = int(input())
    if ascent:
        if prev > h:
            ascent = False
        count += 1
    else:
        if prev < h:
            ascent = True
            count = 2
        else:
            count += 1
    prev = h
    ret = max(ret, count)

print(ret)

"""
貪欲に数えていく
"""
