B = list(map(int, input().split()))
N = int(input())
ret = []
rep = [(B[i], chr(ord("a") + i)) for i in range(10)]
rep.sort()
for i in range(N):
    a = int(input())
    s = "{:10d}".format(a)
    for j in range(10):
        s = s.replace(str(j), rep[j][1])
    ret.append((s, a))
ret.sort()

for _, r in ret:
    print(r)

"""
stringでswapしてしまうことを考える
a~jで置き換えてソート
左埋どうしよう、f stringでいけるか？左0　というか最小値埋め


pypy tleなる？
"""
