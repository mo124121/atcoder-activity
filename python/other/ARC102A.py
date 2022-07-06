N, K = map(int, input().split())

ret = 0

b = 0
for i in range(1, N + 1):
    if i % K == 0:
        b += 1
ret += b**3

if K % 2 == 0:
    c = 0
    for i in range(1, N + 1):
        if i % K == K // 2:
            c += 1
    ret += c**3
print(ret)

"""
考察
2x10^5 -> O(N^2)はだめ

(a+b)%K==0
(b+c)%K==0
(c+a)%K==0
(2(a+b+c))%K==0

とりうるKの倍数の値は2*Nぐらいまで。そこを辞書か何かでとりに行くイメージ？


解説
a%k=b%k=c%k
a%k=0 or a%k=K/2

"""
