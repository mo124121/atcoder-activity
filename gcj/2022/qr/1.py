T = int(input())
ret = [["+"] * 21 for _ in range(21)]
# write -
for i in range(11):
    for j in range(10):
        ret[2 * i][j * 2 + 1] = "-"
# write |
for i in range(10):
    for j in range(11):
        ret[2 * i + 1][2 * j] = "|"


# write .
for i in range(10):
    for j in range(10):
        ret[2 * i + 1][2 * j + 1] = "."
# write . left-upper
ret[0][0] = "."
ret[0][1] = "."
ret[1][0] = "."
ret[1][1] = "."


def show(r, c):
    for i in range(r * 2 + 1):
        print(*ret[i][: c * 2 + 1], sep="")


for t in range(T):
    R, C = map(int, input().split())
    print("Case #{}:".format(t + 1))
    show(R, C)
