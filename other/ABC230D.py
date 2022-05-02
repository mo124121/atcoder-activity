N, D = map(int, input().split())
RL = []
for i in range(N):
    l, r = map(int, input().split())
    RL.append((r, l))
RL.sort()
ret = 0
punched = 0
for r, l in RL:
    if punched < l:
        ret += 1
        punched = r + D - 1

print(ret)


"""
タイトルでふふってなった

直観的にはソートしておきたくなるが、さて

短いの優先？
1.終わる順でソートして、最後+Dの範囲で消せるやつを消していく、とか？

2.それぞれの壁を前後にD延長してもいい
そのうえで座圧？なんか違いそう

わからんから1で実装してみる
あってたわ

解説後
区間スケジューリング問題

"""
