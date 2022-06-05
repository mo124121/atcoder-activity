N = int(input())

ret = 0
prev = 0
for _ in range(N):
    A = int(input())
    if A == 0:
        ret += prev // 2
        prev = 0
    prev += A
ret += prev // 2
print(ret)


"""
小さいほうから貪欲法ではまずいケースはあるか？
ぱっと思いつかないので実装する、はいWA

解説
言われてみれば当たり前だった
"""
