from collections import defaultdict


def check(tower):
    occur = set()
    occur.add(tower[0])
    for i in range(len(tower) - 1):
        if tower[i + 1] in occur and tower[i + 1] != tower[i]:
            return False
        occur.add(tower[i + 1])
    return True


T = int(input())
ret = []

for t in range(T):
    N = int(input())
    S = input().split()
    stock = []
    seen_count = defaultdict(int)
    seen_alph = set()
    pres = defaultdict(lambda: defaultdict(int))
    sufs = defaultdict(lambda: defaultdict(int))
    sps = defaultdict(lambda: defaultdict(int))
    flag_ng = False
    for s in S:
        if s[0] * len(s) == s:
            sps[s[0]][s] += 1
        else:
            pres[s[0]][s] += 1
            sufs[s[-1]][s] += 1
        seen_count[s] += 1

    for s in S:
        if seen_count[s] == 0:
            continue
        seen_count[s] -= 1
        pre = s[0]
        suf = s[-1]
        base = s
        if s[0] * len(s) == s:
            sps[pre][s] -= 1
            if sps[pre][s] == 0:
                del sps[pre][s]
        else:
            pres[pre][s] -= 1
            if pres[pre][s] == 0:
                del pres[pre][s]
            sufs[suf][s] -= 1
            if sufs[suf][s] == 0:
                del sufs[suf][s]

        while True:
            if pre in sps and len(sps[pre]) > 0:
                s2 = next(iter(sps[pre]))
                sps[pre][s2] -= 1
                if sps[pre][s2] == 0:
                    del sps[pre][s2]
                base = s2 + base
                seen_count[s2] -= 1
            elif suf in sps and len(sps[suf]) > 0:
                s2 = next(iter(sps[suf]))
                sps[suf][s2] -= 1
                if sps[suf][s2] == 0:
                    del sps[suf][s2]
                base = base + s2
                seen_count[s2] -= 1
            elif pre in sufs and len(sufs[pre]) > 0:
                s2 = next(iter(sufs[pre]))
                pre2 = s2[0]
                suf2 = s2[-1]
                pres[pre2][s2] -= 1
                if pres[pre2][s2] == 0:
                    del pres[pre2][s2]
                sufs[suf2][s2] -= 1
                if sufs[suf2][s2] == 0:
                    del sufs[suf2][s2]
                base = s2 + base
                pre = pre2
                seen_count[s2] -= 1
            elif suf in pres and len(pres[suf]) > 0:
                s2 = next(iter(pres[suf]))
                pre2 = s2[0]
                suf2 = s2[-1]
                pres[pre2][s2] -= 1
                if pres[pre2][s2] == 0:
                    del pres[pre2][s2]
                sufs[suf2][s2] -= 1
                if sufs[suf2][s2] == 0:
                    del sufs[suf2][s2]
                base = base + s2
                suf = suf2
                seen_count[s2] -= 1
            else:
                break
        stock.append(base)
    tower = "".join(stock)
    if check(tower):
        ret.append(tower)
    else:
        ret.append("IMPOSSIBLE")


for i, r in enumerate(ret):
    print("Case #{:}: {:}".format(i + 1, r))


"""
deque使いながら伸ばしていく？
端と端が同じものを優先してつなげていく
つなげられるものがなくなったらいったんストック
ストックする際に、


まて、この場合だと初回からおかしいやつもあるのか…
追加するときにチェックすればいい
N!パターンあるがどうするか？

とりあえず端が同じやつをキーにつなげて、
大丈夫かどうかチェックすればいいのでは？


"""
