N = int(input())
W = input().split()

T = ["TAKAHASHIKUN", "Takahashikun", "takahashikun"]
ret = 0
for w in W:
    if w[-1] == ".":
        w = w[:-1]
    if w in T:
        ret += 1
print(ret)
