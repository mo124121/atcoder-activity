from collections import defaultdict


N, M, Q = map(int, input().split())

data0 = [0] * (N + 1)
data1 = [0] * (N + 1)
# 区間[l, r)に x を加算
def _add(data, k, x):
    while k <= N:
        data[k] += x
        k += k & -k


def add(l, r, x):
    _add(data0, l, -x * (l - 1))
    _add(data0, r, x * (r - 1))
    _add(data1, l, x)
    _add(data1, r, -x)


# 区間[l, r)の和を求める
def _get(data, k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s


def query(l, r):
    return (
        _get(data1, r - 1) * (r - 1)
        + _get(data0, r - 1)
        - _get(data1, l - 1) * (l - 1)
        - _get(data0, l - 1)
    )


queries = [list(map(int, input().split())) for _ in range(Q)]

# 先読みしてリセットする対応を探す
seen = defaultdict(list)
target = [set() for _ in range(Q)]
for i in range(Q - 1, -1, -1):
    q = queries[i]
    if q[0] == 3:
        seen[q[1]].append(i)
    elif q[0] == 2:
        if q[1] in seen:
            target[i].update(seen[q[1]])
            seen[q[1]] = []

ret = []
ret_tmp = [0] * Q
for i in range(Q):
    q = queries[i]
    if q[0] == 1:
        add(q[1] - 1, q[2], q[3])
    if q[0] == 2:
        for t in target[i]:
            j = queries[t][2]
            ret_tmp[t] -= query(j, j + 1)
    else:
        j = queries[i][2]
        ret.append(query(j, j + 1) - ret_tmp[i])
print(*ret, sep="\n")


#


"""
ベースはfenwickで管理

クエリ先読みして、全体置き換え時に最終的に反映される要素のmapを持っておく
出力の段階が来たら合計の辻褄合わせをする

"""
