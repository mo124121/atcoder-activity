N = int(input())
S = [list(map(int, list(input()))) for _ in range(N)]

ret = 10**10

for d in range(10):  # ターゲットの数字
    max_occ = 0
    i_max = 0
    for i in range(10):  # 左からi番目
        occ = 0
        for j in range(N):  # スロット番号
            occ += int(S[j][i] == d)
        if occ >= max_occ:
            max_occ = occ
            i_max = i
    ret = min(ret, (max_occ - 1) * 10 + i_max)

print(ret)
