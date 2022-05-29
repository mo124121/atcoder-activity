from collections import Counter


H, W, M = map(int, input().split())
seen = set()
count_h = Counter()
count_w = Counter()
for i in range(M):
    h, w = map(int, input().split())
    seen.add((h, w))
    count_h[h] += 1
    count_w[w] += 1

ret = 0
max_w = max(count_w.values())
tmp = {}
for k, v in count_w.items():
    if v == max_w:
        tmp[k] = v
count_w = tmp

max_h = max(count_h.values())
tmp = {}
for k, v in count_h.items():
    if v == max_h:
        tmp[k] = v
count_h = tmp

ret = max_w + max_h
if ret == 0:
    print(ret)
    exit()

for hk in count_h.keys():
    for wk in count_w.keys():
        if (hk, wk) not in seen:
            print(ret)
            exit()

print(ret - 1)


"""
各行・列で個数を合算し、
それが最も多いところが答え
行・列で重複する場合は注意が必要

そこが一番難しいのでは？
仮に全部におかれていた時、
いやおかれた個数に制約があるから問題ないか

とりあえず最大の組み合わせを全探索、
爆破対象がないところがあれば答え

#.#
.#.

"""
