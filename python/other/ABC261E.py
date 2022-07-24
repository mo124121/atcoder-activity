N, C = map(int, input().split())
SIZE = 30
m = (2 << SIZE) - 1
one = m
zero = 0

for i in range(N):
    t, a = map(int, input().split())
    if t == 1:
        one &= a
        zero &= a
    elif t == 2:
        one |= a
        zero |= a
    else:
        one ^= a
        zero ^= a
    C = (C & one) | ((C ^ m) & zero)
    print(C)
