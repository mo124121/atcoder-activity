K = int(input())
S = input()
T = input()

count_remain = [K] * 9
score_A = [0] * 9
count_A = [0] * 9
count_T = [0] * 9

for c in S:
    if c != "#":
        c = int(c) - 1
        count_remain[c] -= 1
        count_T[c] += 1
for c in T:
    if c != "#":
        c = int(c) - 1
        count_remain[c] -= 1
        count_A[c] += 1

for i in range(9):
    if count_remain[i] > 0:
        count_A[i] += 1
        for j in range(9):
            score_A[i] += (1 + j) * 10 ** count_A[j]
        count_A[i] -= 1

pat_count = 0
win_count = 0

for a in range(9):
    if count_remain[a] == 0:
        continue
    pat = count_remain[a]
    count_remain[a] -= 1

    for t in range(9):
        if count_remain[t] == 0:
            continue
        pat *= count_remain[t]
        pat_count += pat
        count_T[t] += 1
        score = 0
        for i in range(9):
            score += (i + 1) * 10 ** count_T[i]
        if score > score_A[a]:
            win_count += pat
        count_T[t] -= 1
        pat //= count_remain[t]
    count_remain[a] += 1

print("{:.7f}".format(win_count / pat_count))

"""
がっつり期待値

お互い#がある中で、残っている手札の確率から何を引く形になるか考える？

1.青木君が0~9のそれぞれを引く期待値とスコアを求める
2.高橋君が残されたものを引くときの選択肢のうち、青木君の超えられる手の割合
たぶん全列挙でいいわ

"""
