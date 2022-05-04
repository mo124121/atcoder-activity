MOD = 998244353
N = int(input())
F = [-1] + list(map(int, input().split()))

loop_count = 0
seen = set()
for i in range(1, N + 1):
    if i in seen:
        continue
    current = set()
    current.add(i)
    nx = F[i]
    while nx not in seen:
        if nx in current:
            loop_count += 1
            break
        current.add(nx)
        nx = F[nx]

    seen.update(current)


if loop_count == 0:
    print(0)
else:
    print(pow(2, loop_count, MOD) - 1)


"""
数学くさい

要するにループしている感じがよいのでは
f(a)!=f(b)の時点で、ループに入っていく系はNG

別にループしている必然性はない？いや必要
一度見たところについたらループをカウント
新規ループなのか旧ループなのか区別する必要はある

TLEがとれないあきらめる
"""
