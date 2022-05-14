W = int(input())

A = [i + 1 for i in range(2**7 - 1)]

B = [(i + 1) << 7 for i in range(2**6 - 1)]
C = [(i + 1) << 13 for i in range(2**6 - 1)]


A = A + B + C
N = len(A)
print(N)
print(*A)

ret = set()
for i in range(N):
    ret.add(A[i])
    for j in range(N):
        if i == j:
            continue
        ret.add(A[i] + A[j])
        for k in range(N):
            if i == k or j == k:
                continue
            ret.add(A[i] + A[j] + A[k])

print(ret)

"""
逆に1,Wに到達可能な組み合わせを考える
300個以内で
W<=10**6

bitで表現して、3つで全ての値を表現できるか？
10**6==2**20
とりあえず

3つの桁ブロックに分割
7 6 6
2**7=128
たぶんギリギリ足りる

"""
