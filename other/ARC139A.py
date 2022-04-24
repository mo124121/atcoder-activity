N = int(input())
T = list(map(int, input().split()))

A = 1 << T[0]

for i in range(N - 1):
    if T[i] > T[i + 1]:
        A += 1 << T[i + 1]
    else:
        A -= A & ((1 << (T[i + 1])) - 1)
        if (A >> T[i + 1]) & 1 == 0:
            A += 1 << T[i + 1]
        else:
            A += 1 << (T[i + 1] + 1)

print(A)


"""
上位のbitをうまく使っていくイメージ
前のAiを保存しつつ、どこかのbitを立てる形で調整をしていく
Ti<=Ti+1 -> 下を0埋めしつつ、Ti+1以上の桁のところで0のbitを探して立てる
Ti>Ti+1 該当のbitを立てる

"""
