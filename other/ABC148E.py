N = int(input())

if N % 2 == 1 or N < 10:
    print(0)
    exit()

ret = 1
start = 10
top = bot = start
while True:
    if bot > N:
        break
    top *= 10
    ret += min(top, N) // 10 - 1
    bot = top
print(ret)


"""
N<10**18ででかい
法則を見つけるべき
0が並ぶ=10を因数に持つ -> C*2^M*5^N 答えmin(M,N)

f(n)=nf(n-2)
n=奇数の時、2が出てこない min(0,N)->0

おそらく、M>N 実質Nの個数を数え上げればいい
そして出てくるのは10の倍数の時（奇数はでない=5だけの倍数は出てこないので）


解説後
発想は正しい

"""
