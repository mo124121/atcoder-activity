from itertools import permutations


X, Y, A, B, C = map(int, input().split())


def yes():
    print("Yes")
    exit()


###横×3
if (A + Y - 1) // Y + (B + Y - 1) // Y + (C + Y - 1) // Y <= X:
    yes()

###縦x3
if (A + X - 1) // X + (B + X - 1) // X + (C + X - 1) // X <= Y:
    yes()

###縦横横
for a, b, c in permutations((A, B, C)):
    x = X - (a + Y - 1) // Y
    if x > 0 and (b + x - 1) // x + (c + x - 1) // x <= Y:
        yes()
# 横縦縦
for a, b, c in permutations((A, B, C)):
    y = Y - (a + X - 1) // X
    if y > 0 and (b + y - 1) // y + (c + y - 1) // y <= X:
        yes()
print("No")


"""
横横横
縦縦縦
縦横横
縦縦横
みたいな配置、ABC全部試す

"""
