import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")

S = [input() for _ in range(3)]


def no():
    print("UNSOLVABLE")
    exit()


def yes(T):
    for i in range(3):
        print(T[i])
    exit()


chars = set()
for s in S:
    chars.update(s)
chars = list(chars)
if len(chars) > 10:
    no()

used = set()


def rec(T, i):
    if i == len(chars):
        if int(T[0]) + int(T[1]) == int(T[2]):
            yes(T)
        else:
            return False

    for j in range(10):
        if j not in used:
            used.add(j)
            for k in range(3):
                T[k] = T[k].replace(chars[i], str(j))
            if "0" not in [T[i][0] for i in range(3)]:
                rec(T, i + 1)
            for k in range(3):
                T[k] = T[k].replace(str(j), chars[i])
            used.discard(j)


rec(S, 0)
no()

"""
はじめてのふくめんざん


違う文字は違う数字という制約があるので、
10文字を超えたらout
10!のパターンを試していく
これメモリたりる…？
"""
