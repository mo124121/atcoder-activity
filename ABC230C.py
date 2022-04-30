N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())
ret = []
for i in range(P, Q + 1):
    line = []
    for j in range(R, S + 1):
        if A - B == i - j or A + B == i + j:
            line.append("#")
        else:
            line.append(".")
    ret.append(line)
for r in ret:
    print(*r, sep="")

"""
非初見

取り出す範囲だけ眺めたらよろしい

"""
