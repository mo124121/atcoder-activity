N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

ret = False
# ずらす量　高さ
for shift_h in range(N - M + 1):
    # ずらす量　幅
    for shift_w in range(N - M + 1):
        # マッチ確認
        flag = True
        for h in range(M):
            for w in range(M):
                if A[shift_h + h][shift_w + w] != B[h][w]:
                    flag = False
                    break
        if flag:
            print("Yes")
            exit()

print("No")

"""
マジでやるならローリングハッシュ

ただ小さいN,M<50で小さい
間に合うか見積もる->面倒なのでとりあえずごり押しで実装
書いてからわかるがN**2*M**2 < 10**7ぐらい？

"""
