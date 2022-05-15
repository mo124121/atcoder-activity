W = int(input())

A = [i + 1 for i in range(100)]

B = [(i + 1) * 10**2 for i in range(100)]
C = [(i + 1) * 10**4 for i in range(100)]


A = A + B + C
N = len(A)
print(N)
print(*A)

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
