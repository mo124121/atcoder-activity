T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    shift = 0
    i = N
    lines = [[] for _ in range(4)]
    lines[0].append((0, 0))
    while i > 1:
        lines_next = [[] for _ in range(4)]
        for e in range(4):
            for v, count in lines[e]:
                if v + 2 <= K:
                    lines_next[e].append((v + 2, count + 1))
                    if v + i - 1 <= K:
                        lines[(e + 1) % 4].append((v + i - 1, count))
                if e == 3 and v + i <= K:
                    lines_next[0].append((v + i, count))
        for e in range(4):
            lines[e] = lines_next[e]
        i -= 2
    ret = []
    for line in lines:
        for v, count in line:
            if v == K:
                ret.append(count)
    if len(ret) == 0:
        print("Case #{:d}:".format(t + 1), "IMPOSSIBLE")
    else:
        print("Case #{:d}:".format(t + 1), len(ret))
        print(*ret)


"""
スキップできる数は外周からの距離でたぶん決まる
N**2のdpテーブルは厳しい

中の周回までのずらせる遷移を考える
特定の倍数しか遷移できない->dp
dp[]

"""
