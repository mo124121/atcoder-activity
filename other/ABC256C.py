h1, h2, h3, w1, w2, w3 = map(int, input().split())
ret = 0
for v11 in range(1, 31):
    for v12 in range(1, 31):
        v13 = w1 - v11 - v12
        if v13 <= 0:
            continue
        for v21 in range(1, 31):
            v31 = h1 - v11 - v21
            if v31 <= 0:
                continue
            for v22 in range(1, 31):
                v23 = w2 - v21 - v22
                v32 = h2 - v12 - v22
                v33 = w3 - v31 - v32
                if v23 <= 0 or v32 <= 0 or v33 <= 0:
                    continue
                if v33 == h3 - v13 - v23:
                    ret += 1

print(ret)
