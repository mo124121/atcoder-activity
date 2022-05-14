T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    if K % 2 == 1:
        print("Case #{:d}:".format(t + 1), "IMPOSSIBLE")
        continue
    ret = []
    M = N**2 - 1
    i = N
    j = 0
    while i > 3:
        j_diff = 4 * (i - 1)
        k = 0
        if M - K >= j_diff - 2:
            M -= j_diff - 2
            ret.append((j + 1, j + j_diff))
        else:
            for k, e in enumerate([4, 6, 8]):
                if M - K >= j_diff - e:
                    M -= j_diff - e
                    ret.append(
                        (j + (i - 1) * (k + 1) + 2, j + j_diff + 1 + (i - 3) * (k + 1))
                    )
                    break

        i -= 2
        j += j_diff

    for e in [6, 4, 2]:
        if M - K == e:
            M -= e
            ret.append((N**2 - 1 - e, N**2))
            break
    if M == K:
        print("Case #{:d}:".format(t + 1), len(ret))
        for r in ret:
            print(*r)
    else:
        print("Case #{:d}:".format(t + 1), "IMPOSSIBLE")

"""
スキップできる数は外周からの距離でたぶん決まる
N**2のdpテーブルは厳しい

中の周回までのずらせる遷移を考える
特定の倍数しか遷移できない->dp
dp[]

"""
