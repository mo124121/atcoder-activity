N, M = map(int, input().split())
if M == 0:
    print(0)
    exit()


def calc(x, r):
    ret_x = 2 * x * r + (r**2 // M)
    ret_r = r**2 % M
    return ret_x, ret_r


base = 10
i = 0
x = 10 // M
r = 10 % M

ret = 0
while 2**i <= N:
    if (N >> i) & 1 == 1:
        ret = (ret + x) % M
    i += 1
    x, r = calc(x, r)
print(ret)
"""
式変形が大事

10**N // M % M

繰り返し2乗法っぽい
10**4 // M % M

先にMODとってからしたらまずいっすか？

商とあまりに分割して考えるとか？

A[i]=M*X[i]+R[i]
A[i+1]=M*X[i+1]+R[i+1]
=A[i]**2=(M*X[i])**2 + 2*M*X[i]*R[i]+R[i]**2
=M*(M*X[i]**2+2*X[i]*R[i]+R[i]**2//M)+R[i]**2%M

X[i+1]=M*X[i]**2+2*X[i]*R[i]+R[i]**2//M
R[i+1]=R[i]**2%M

たぶんこのあまりの2乗しか残らない->繰り返し2乗法で計算、
最後にNのbitが立っているところで足しこんで行く
混乱してた、これは誤り



M==1のときはあまり0
"""
