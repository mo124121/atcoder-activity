N = int(input())
A = list(map(int, input().split()))
ret = -(10**10)
for i in range(N):
    r = 0
    score_a_max = -(10**10)
    for j in range(N):
        if i == j:
            continue
        if i < j:
            x, y = i, j
        else:
            x, y = j, i
        s = [0] * 2
        for k in range(y - x + 1):
            s[(1 + k) % 2] += A[k + x]
        if score_a_max < s[0]:
            score_a_max = s[0]
            r = s[1]
    ret = max(ret, r)

print(ret)
"""
全探索

青木がとれるうちベストなときの高橋のスコアが
各高橋の選択の結果
これの最大値を更新していく

ACしたけどバグらせすぎ

"""
