N = int(input())
R = []
G = []
B = []

for i in range(2 * N):
    a, c = input().split()
    a = int(a)
    if c == "R":
        R.append(a)
    elif c == "G":
        G.append(a)
    else:
        B.append(a)
if len(R) % 2 == 0 and len(G) % 2 == 0 and len(B) % 2 == 0:
    print(0)
    exit()
R.sort()
G.sort()
B.sort()
INF = 10**15


def search_min(C1, C2):
    i1 = 0
    i2 = 0

    ret = INF
    while i1 < len(C1):
        while i2 < len(C2):
            ret = min(ret, abs(C1[i1] - C2[i2]))
            if C1[i1] < C2[i2]:
                break
            else:
                i2 += 1
        i1 += 1
    return ret


C = [R, G, B]
for i in range(3):
    if len(C[i]) % 2 == 0:
        if len(C[i]) == 0:
            print(search_min(C[(i + 1) % 3], C[(i + 2) % 3]))
        else:
            odd_odd = search_min(C[(i + 1) % 3], C[(i + 2) % 3])
            odd_even1 = search_min(C[(i) % 3], C[(i + 2) % 3])
            odd_even2 = search_min(C[(i + 1) % 3], C[(i) % 3])
            print(min(odd_odd, odd_even2 + odd_even1))
        exit()


"""
総和の最小値　2分探索？なんか違いそう

おっきい方から同じ色として入れていく感じ？貪欲法
同じ色でペアが作れるのにわざわざ別の組み合わせる必要はない
一番小さいやつでペア作る　→　あかん　絶対値の差が一番小さくなるやつにする必要がある
奇数のやつ同士だけで考えてもいけない、R-G,G-Bで絶対値の差が一番小さくなるケースもある

逆に
R-Bで差が最小のケースと、R-G,G-Bで差が最小になるケースで網羅されるはず
全部2の倍数->0
それ以外、各色ペアで最小差計算して、min(odd-odd,even-odd,even-odd)
ソートして最小差するなら尺取り法的にできる？
"""
