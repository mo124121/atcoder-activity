def solve(N, A):
    A.sort()
    m, p = A[0], A[-1]
    ops = []
    for a in A[1:-1]:
        if a < 0:
            ops.append((p, a))
            p -= a
        else:
            ops.append((m, a))
            m -= a
    ops.append((p, m))
    return p - m, ops


def main():
    N = int(input())
    A = list(map(int, input().split()))
    v, ops = solve(N, A)

    print(v)
    for op in ops:
        print(*op)


main()

###


"""
heapっぽい　理屈はわからない

なるべく大きい数字は大きいまま残してxにすべき
あーでも負の数があるのか
最大のマイナスに対してプラスをすべて引く
最大のプラスに対してマイナスをすべて引く　残りが答え


全てマイナスの時
一番絶対値が小さい値をxにしてそのあと全部引いて行く

全てがプラスの時
でっかいマイナスを作って最後にマイナスする
一番小さい値をxにして、一度マイナスの世界に行く
2番目に小さいのをxにして、マイナスで大きなのを元の世界に戻す

少し場合分けが大変だが書いていく

自力AC

最短のコードが賢い

"""
