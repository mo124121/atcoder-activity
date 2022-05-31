from collections import deque


def solve(N, A):
    if N == 2:
        ops = [(max(A), min(A))]
        v = max(A) - min(A)
        return v, ops

    ps = []
    ms = []
    for a in A:
        if a >= 0:
            ps.append(a)
        else:
            ms.append(a)
    ps.sort()
    ms.sort(reverse=True)

    ps = deque(ps)
    ms = deque(ms)
    ops = []
    if len(ps) == 0:
        x = ms.popleft()
        y = ms.popleft()
        ps.append(x - y)
        ops.append((x, y))

    if len(ms) == 0:
        x = ps.popleft()
        y = ps.popleft()
        ms.append(x - y)
        ops.append((x, y))

    while len(ps) > 1:
        x = ms.pop()
        y = ps.popleft()
        ms.append(x - y)
        ops.append((x, y))

    while len(ms) > 0:
        x = ps.pop()
        y = ms.popleft()
        ps.append(x - y)
        ops.append((x, y))

    return ps.pop(), ops


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
