N = int(input())
tower = []
for _ in range(N):
    w = int(input())
    target = -1
    m = 10**10
    for i, t in enumerate(tower):
        if t[-1] >= w and t[-1] < m:
            target = i
            m = t[-1]
    if target != -1:
        tower[target].append(w)
    else:
        tower.append([w])
print(len(tower))


"""
トラックから運ぶ順で考えるので、
とりあえず既存の山で乗るうちの最も軽いやつに突っ込んでいく感じ
小さいし楽勝かな・・？
N<50

本当に貪欲法でいい？とりあえずやってみる

"""
