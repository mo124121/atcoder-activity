N = int(input())

ret = 0
for k in range(1, 18):
    base = int("1" * k)
    if base > N:
        break
    top = bot = base
    ret += 1

    while True:
        bot *= 10
        top = (top + 1) * 10 - 1

        if N < bot:
            break

        ret += min(N, top) - bot + 1

print(ret)


"""
N<10**15

桁が増えるごとに計算してみる

先頭桁数×パターン数

先頭桁数は制御できる

二つ下以下のとりうる範囲で考える


1 1x1
10 1x1
11 2x1
100~109 1x10
110,112~119 2x9
111 3x1
1000~1099
1100~1199
1110,1112~1119
1111
次の開始と最終桁がややこし

解説後
続く数をベースに考えるほうがシンプルっぽい

"""
