from bisect import bisect

Q = int(input())
ret = []
N = 2**20
A = [-1] * (N)
B = [1] * (N)
for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        h = bisect(B, -1, x % N)
        if h == N:
            h = bisect(B, -1)
        A[h] = x
        B[h] = -1
    if t == 2:
        ret.append(A[x % N])
print(*ret, sep="\n")

"""
N=2**20->10**6
bisectや

んーなんか違う
同じやつを刺された時のポインタみたいなのが欲しい 一番右はこいつ、的な

bisectでできてる気がするが、
16WA/18
結構根本的に間違えている？



"""
