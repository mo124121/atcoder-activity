N = int(input())
S = [[list(input()) for _ in range(N)]]
T = [[list(input()) for _ in range(N)]]


def rotate(U):
    R = [["."] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            R[i][j] = U[j][-1 - i]
    return R


def shift_corner(U):
    h_shift = 0
    for i in range(N):
        if "#" in U[i]:
            break
        h_shift += 1

    v_shift = 0
    for j in range(N):
        flag = False
        for i in range(N):
            if U[i][j] == "#":
                flag = True
                break
        if flag:
            break
        v_shift += 1

    U = U[h_shift:] + U[:h_shift]
    for i in range(N):
        U[i] = U[i][v_shift:] + U[i][:v_shift]
    return U


def same(U, V):
    for i in range(N):
        for j in range(N):
            if U[i][j] != V[i][j]:
                return False
    return True


for i in range(3):
    S.append(rotate(S[i]))
    T.append(rotate(T[i]))

for i in range(4):
    S[i] = shift_corner(S[i])
    T[i] = shift_corner(T[i])

for k in range(4):
    for l in range(4):
        if same(S[k], T[l]):
            print("Yes")
            exit()

print("No")
"""
zobrist hashしか思いつかない脳

回転させた４パターンを作る
左上に寄せる
各ハッシュを計算する　4**2*200**2　大した数じゃないのでhashじゃなくていい
一致を見る

AC
解説後
#がある位置を持っておいて、ガチャガチャするほうが楽
"""
