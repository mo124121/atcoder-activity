N = int(input())

if N == 0:
    print(0)
    exit()
elif N > 0:
    sgn = -1
else:
    sgn = 1
M = abs(N)

ret = []
TS = []
i = 0
kuriagari = 0

deb_1 = 0
deb_2 = 0
while 2 ** (i - 2) <= M:
    t = (M >> i) & 1
    s = t ^ kuriagari
    if sgn > 0:
        kuriagari = t | s
    else:
        kuriagari = t & ~s
    ret.append(s)
    if True:
        TS.append((t, s))
        deb_1 += t * 2**i
        deb_2 += s * (-2) ** i
    i += 1
    sgn *= -1

for i in range(2):
    if ret[-1] == 0:
        ret.pop()

print(*reversed(ret), sep="")


"""
ノートで考察して自力AC
 2のbitの世界のΣ=N
-2のbitの世界のΣ=N
の差をとると、Σ-Σ=N-N=0

そうすると、2の世界のbitが立つのに対して、
それを消しこむために、
-2のbitをどう立てたらいいかを考えていく問題になる

場合分けして考えると消しこめる

解説の考えもすごい大事
"""
