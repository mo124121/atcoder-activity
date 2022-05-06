N = int(input())
S = list(map(int, list(input())))
T = list(map(int, list(input())))


r = 1
for l in range(N):
    if S[l] != T[l]:
        while r < N:

            r += 1


"""
右から貪欲じゃだめ？そんなに簡単な問題ではなさそう
左で操作してから右を操作しないといけないケースがありそう

逆に左から埋めていく？

できない条件を考えると、
操作によって1は増やせない
1を右には動かせない

尺取り法っぽい

左のほうに埋めていく


"""
