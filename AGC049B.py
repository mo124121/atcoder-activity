N = int(input())
S = list(map(int, list(input())))
T = list(map(int, list(input())))


r = 1
ret = 0
for l in range(N):
    if r <= l:
        r = l + 1
    if S[l] == 1 and T[l] == 0:
        while r < N:
            if S[r] == 1:
                S[l] = 0
                S[r] = 0
                ret += r - l
                break
            r += 1
        r += 1
    elif S[l] == 0 and T[l] == 1:
        while r < N:
            if S[r] == 1:
                S[l] = 1
                S[r] = 0
                ret += r - l
                break
            r += 1
        r += 1
if S == T:
    print(ret)
else:
    print(-1)


"""
右から貪欲じゃだめ？そんなに簡単な問題ではなさそう
左で操作してから右を操作しないといけないケースがありそう

逆に左から埋めていく？

できない条件を考えると、
操作によって1は増やせない
1を右には動かせない

尺取り法っぽい

左のほうに埋めていく

16/34 WA
考慮が抜けてる系

AC


"""
