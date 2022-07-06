A, B, C, X, Y = map(int, input().split())
Z = 0
ret = A * X + B * Y
while X > 0 or Y > 0:
    if X > 0 and Y > 0:
        if A + B > 2 * C:
            ret -= A + B
            ret += 2 * C
            X -= 1
            Y -= 1
            Z += 2
        else:
            break
    elif X > 0:
        if A > 2 * C:
            ret -= A
            ret += 2 * C
            X -= 1
            Z += 2
        else:
            break
    elif Y > 0:
        if B > 2 * C:
            ret -= B
            ret += 2 * C
            Y -= 1
            Z += 2
        else:
            break

print(ret)
