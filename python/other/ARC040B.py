N, R = map(int, input().split())
S = input()
T = []
for i, s in enumerate(S):
    if s == ".":
        T.append(i)
if not T:
    print(0)
    exit()

final_pos = max(T[-1] - R + 1, 0)
now = 0
filled = -1
ret = 0
for t in T:
    if t >= final_pos:
        ret += final_pos - now
        ret += 1
        break
    if t <= filled:
        continue
    # move
    ret += t - now
    now = t
    # shoot
    filled = now + R - 1
    ret += 1

print(ret)

"""
最後に塗るべきところまでは移動しなくていい

"""
