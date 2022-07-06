from collections import defaultdict, deque


N = int(input())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

if N == 1:
    print(1)
    exit()

ret = 10**10
diff_count = defaultdict(int)
for x1, y1 in zip(X, Y):
    for x2, y2 in zip(X, Y):
        if (x1, y1) == (x2, y2):
            continue
        p = x2 - x1
        q = y2 - y1
        diff_count[(p, q)] += 1


for v in diff_count.values():
    ret = min(ret, N - v)
print(ret)
"""
Nが小さい
とりあえず全ペアの差が候補
条件を満たす場合はコスト0,満たさない場合はコスト1で遷移できるグラフ問題？
ダイクストラまたは01DFSで探す

解説後
そもそも差が同じじゃなければつながなくていい
UFあたりでもよさそうで連結を見るだけでもいい
"""
