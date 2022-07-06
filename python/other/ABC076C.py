S = list(input())
T = input()
replaced = False
for i in reversed(range(len(S))):
    flag = True
    for j, t in enumerate(T):
        if i + j >= len(S) or S[i + j] not in (t, "?"):
            flag = False
            break
    if flag:
        for j, t in enumerate(T):
            S[i + j] = t
        replaced = True
        break

if replaced:
    print("".join(S).replace("?", "a"))
else:
    print("UNRESTORABLE")

"""
まあ文字数は少ない <50

???をTを用いて置換できる部分があるか？
別に最初から含まれていてもいい

辞書順最小->aで置換する


一つずつづらしてチェックするごり押しがよさそう


WA　何か？
辞書順がミソ
複数マッチするケースで、先頭からマッチするとaより大きくなる場合がある
"""
