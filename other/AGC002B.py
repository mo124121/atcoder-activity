N, M = map(int, input().split())
seen = set()
seen.add(1)
count = [1] * (N + 1)

for i in range(M):
    x, y = map(int, input().split())
    if x in seen:
        seen.add(y)
    count[x] -= 1
    count[y] += 1
    if count[x] == 0:
        seen.discard(x)

print(len(seen))


"""
移動する可能性があるというにボールの個数が関与するのがミソ
ただまあ、ボールが1個しかなかったら滞留できないよ、という話



"""
