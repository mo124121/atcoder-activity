N = int(input())
a = list(map(int, input().split()))
INF = 10**5
ret = -INF
score = [0] * 2
for i in range(N):
    a_max = (-INF, -1, i, -INF)
    for j in range(N):
        if i == j:
            continue
        score[0] = score[1] = 0
        for k in range(min(i, j), max(i, j)):
            score[(1 + k) % 2] += a[k]
        a_max = max(a_max, (score[1], -j, i, score[0]))
    ret = max(ret, a_max[3])
print(ret)


"""
先行操作
後攻は自分のスコア最大化することを目的としていて、相互作用はない

N<50　小さい
もうごり押しでいいじゃん

偶奇の操作は後攻もする可能性がある　これは全探索したほうが抜け漏れなさそう

ただ、反転が多い問題、ややこしい
問題設定どおりの挙動をさせるべき

"""
