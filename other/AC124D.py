from collections import deque


def solve(K, S):
    S = list(map(int, list(S)))
    prev = -1
    count = 0
    T = []
    for c in S:
        if prev != c:
            if count > 0:
                T.append((prev, count))
            prev = c
            count = 0
        count += 1
    T.append((prev, count))

    k = 0
    q = deque()
    ret = 0
    r = 0
    for bit, c in T:
        q.append((bit, c))
        r += c
        if bit == 0:
            k += 1
            while k > K:
                bi, ci = q.popleft()
                r -= ci
                if bi == 0:
                    k -= 1

        ret = max(ret, r)
    return ret


def submit():
    N, K = map(int, input().split())
    S = input()
    ret = solve(K, S)
    print(ret)


submit()

"""
連続したビットを何本立てられるか？

反転させる理由はあるか？
0000000000100000000000
1111111111011111111111
1111111111111111111111

1111111111100000000000
1111111111111111111111

あんまりないように見える、結局0埋め

なるべく長いところから埋めていく？

いったん1がx個、0がy個みたいな感じで考えていく
0のkブロック分ずらしながら、最大を探す

そこそこWA

反転パターンも考えるべき？あんまり意味ある感じしないんだよな

解説後
考え方は普通にあってた

"""
