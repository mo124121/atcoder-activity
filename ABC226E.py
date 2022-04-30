from collections import defaultdict, deque


N, M = map(int, input().split())
MOD = 998244353
G = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

ret = 1

q = deque()
seen = set()
for i in range(1, N + 1):
    if i in seen:
        continue
    q.append(i)
    seen.add(i)
    seen_count = 0
    j = 0
    while len(q):
        j += 1
        node = q.popleft()
        for neibor in G[node]:
            if neibor in seen:
                seen_count += 1
            else:
                seen.add(neibor)
                q.append(neibor)
    if seen_count - j == 1:
        ret = ret * 2 % MOD
    else:
        ret = 0
        break
print(ret)


"""
水色っぽいレベル感
M<2*10**5

もちろんできないケースもある

外から入る個数は気にしなくていい

有効グラフに変換したときに条件を満たすグラフの個数

向きを決めてしまった辺はつかえない

なんか逆向きで考えるほうがやりやすそう？


ソートの問題に置き換える？


入力例4の感じだとなんかパターンが少ない

N,Mがでかいので、ノード毎の問題に置き換えたい

Π(辺の数-1)とか？だめ？
出島みたいなところは消すイメージ

ループの個数×2とか？
でもループしているかどうかは大事
   3
1 2 4 

5 6
 7

二つのループは作れない
連結成分の中で、ループとそこにいたる何かのパターン

やっぱり少ない
全ての辺に方向をつける以上２つ以上ループがあったら作れなくなるはず
各連結成分にちょうど1つのループがあるケースだけ　２パターン
連結成分

複数ループがある->1度見たことある場所に2回以上たどり着く

"""
