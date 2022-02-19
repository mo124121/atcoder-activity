T = int(input())

ret = []
for i in range(T):
    N = int(input())
    S = [input() for _ in range(3)]
    ret.append("1" * N + "0" * N + "1")

print(*ret, sep="\n")
