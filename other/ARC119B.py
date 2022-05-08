N = int(input())
S = list(map(int, list(input())))
T = list(map(int, list(input())))

if sorted(S) != sorted(T):
    print(-1)
    exit()

count_list = [[] for _ in range(2)]
l = 0
r = 0
while l < N:
    while r < N and S[l] == S[r]:
        r += 1
    count_list[S[l]].append([r - 1, r - l])
    l = r

ret = 0
current = [count_list[0].pop(), count_list[1].pop()]
for i in range(N - 1, -1, -1):
    t = T[i]
    if current[t][0] != 0:
        current[1 - t][0] -= 1
        ret += 1
    current[t][0] -= 1
    current[t][1] -= 1
    if current[t][1] == 0:
        if len(count_list[t]) == 0:
            print(ret)
            exit()
        current[t] = count_list[t].pop()


"""
00001->10000
11110->01111

操作で増減はできない->1の数が合わないのは-1

貪欲にやっていくのがいい？　が間に合わない
N<5*10**5

とりあえず圧縮した表を持っておいて、
順次消化していくとか
いずれにせよ1個ずつしか動かせない
テーブルを活用して埋めていく

間違ってますねはい

移動量の最大化を狙う
うまくやると1度できる操作が2つに分割されてしまうイメージ

発想の問題な気がする解説見る
あー問題よみまちがえてるーーーー

"""
