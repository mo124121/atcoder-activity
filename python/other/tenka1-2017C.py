N = int(input())
M = 3501

for h in range(1, M):
    for w in range(1, M):
        tmp = 4 * h * w - N * (h + w)
        if tmp > 0:
            if N * h * w % tmp == 0:
                u = N * h * w // tmp
                if u < M:
                    print(h, u, w)
                    exit()


"""
4/N=1/h+1/n+1/w
nhw<3500
式変形してwとhをずらして全探索
w*h<10**7ぐらいなので間に合う
"""
