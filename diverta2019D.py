N = int(input())
ret = 0
r = 1
prev = N
while r**2 <= N:
    if (N - r) % r == 0 and (N - r) // r > r:
        ret += (N - r) // r
    r += 1
print(ret)

"""
考察
N<10**12

Nの線形探索はできない
一方で線形探索できたら答えはでる

いかに効率化するか？

floor(N/m)=N mod m

in1
8

1 8 0
2 4 0
3 2 2 !
4 2 0
5 1 3
6 1 2
7 1 1 !
8 1 0


とりあえず素因数は飛ばせる　なんにせよ0

15
1 15 0
2  7 1
3  5 0
4  3 3 !
5  3 0
6  2 3
7  2 1
8  1 7
9  1 6
10 1 5
11 1 4
12 1 3
13 1 2
14 1 1 !
15 1 0

逆に考えるのは？
x -> N-mx=m  -> m = N/(x+1)


N//m = x
N//n = x-1
N=mx
N=n(x-1)
n =x//(x-1)m

解説後
約数かあ

"""
