N = int(input())
S = [[input() for _ in range(N)]]
T = [[input() for _ in range(N)]]


def rotate(U):
    pass


def shift_corner(U):
    pass


def same(U, V):
    pass


for i in range(3):
    S.append(rotate(S[i]))
    T.append(rotate(T[i]))

for i in range(4):
    shift_corner(S[i])
    shift_corner(T[i])

for i in range(4):
    for j in range(4):
        if same(S[i], T[j]):
            print("Yes")
            exit()

print("No")
"""
zobrist hashしか思いつかない脳

回転させた４パターンを作る
左上に寄せる
各ハッシュを計算する　4**2*200**2　大した数じゃないのでhashじゃなくていい
一致を見る


"""
