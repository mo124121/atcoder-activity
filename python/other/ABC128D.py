N, K = map(int, input().split())
V = list(map(int, input().split()))

ret = -(10**18)

for l in range(N + 1):
    for r in range(N + 1):
        if l + r > N:
            break
        rest = K - l - r
        if rest < 0:
            break

        has = V[:l] + V[N - r :]
        has.sort()
        r = sum(has)
        for i in range(min(rest, len(has))):
            if has[i] >= 0:
                break
            r -= has[i]
        ret = max(ret, r)
print(ret)


"""
回数・dequeを左右に割り振るイメージ？
もう少し賢くやりたい

dpl:片方からの見たときにK回の走査でできる最大値


解説見る
シンプルだった
"""
