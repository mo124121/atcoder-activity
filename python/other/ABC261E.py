N, C = map(int, input().split())
SIZE = 30
op = [[0, 1] for _ in range(SIZE)]

for i in range(N):
    t, a = map(int, input().split())
    for bit in range(SIZE):
        if t == 1:
            op[bit][0] &= a >> bit & 1
            op[bit][1] &= a >> bit & 1
        elif t == 2:
            op[bit][0] |= a >> bit & 1
            op[bit][1] |= a >> bit & 1
        else:
            op[bit][0] ^= a >> bit & 1
            op[bit][1] ^= a >> bit & 1
    X = 0
    for bit in range(SIZE):
        X += op[bit][C >> bit & 1] << bit
    C = X
    print(C)
