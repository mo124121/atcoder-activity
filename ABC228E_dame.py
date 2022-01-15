N,K,M=map(int,input().split())

MOD=998244353

import math
MAX_RANGE= math.log2(10**18)+1

k_n = 1
buf = K % MOD
for i in range(int(MAX_RANGE+1)):
    if N & (1 << i):
        k_n = (k_n*buf) % MOD
    buf = (buf * buf) % MOD

ret = 1
buf = M  % MOD
if buf == 0:
    print(buf)
    exit()
for i in range(int(MAX_RANGE+1)):
    if k_n & (1 << i):
        ret = (ret*buf) % MOD
    buf = (buf *buf) % MOD

print(ret)