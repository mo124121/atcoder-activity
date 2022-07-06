S = input()
T = input()

cooc_S = {}
cooc_T = {}
for i in range(len(S)):
    if S[i] not in cooc_S:
        cooc_S[S[i]] = T[i]
    else:
        if cooc_S[S[i]] != T[i]:
            print("No")
            exit()
    if T[i] not in cooc_T:
        cooc_T[T[i]] = S[i]
    else:
        if cooc_T[T[i]] != S[i]:
            print("No")
            exit()
print("Yes")


"""
種類を減らす方向はたぶんできる　いやできない
SとTの間の同じ文字位置の文字対応関係がずれてなければできる？
証明できんが一度やってみる

逆向きも考える必要がありそう

"""
