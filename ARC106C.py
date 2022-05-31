N, M = map(int, input().split())


ret = []
if M == 0:
    for i in range(N):
        ret.append((2 * i + 1, 2 * i + 2))
elif abs(M) >= N - 1 or M < 0:
    print(-1)
    exit()
else:
    for i in range(N - 1):
        ret.append((3 * i + 2, 3 * i + 4))
    ret.append((1, (M + 1) * 3))

for r in ret:
    print(*r)


"""
方針転換
2コと1コをペアにして作る
左からとると1個しか取れないが、右からとると2個とれるイメージ

いやたぶんあってるわ

解説AC
問題文をよく読むべき

あと最適化的に取れない場合を考えるべき
ただ、区間スケジューリング問題に相当することを察知するのは少し厳しい
それに気づければM<0はあり得ないというのは割と自明
"""
