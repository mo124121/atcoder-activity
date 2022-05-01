N = int(input())
A = list(map(int, input().split()))

B = [0] * N
i = 1
for a in A:
    B[0] += i * a
    i *= -1

for i in range(1, N):
    B[i] = A[i - 1] * 2 - B[i - 1]

print(*B)

"""
ループする山脈

N<10**5

sum(B)=sum(A)
A1=(B1+B2)//2 2*A1=B1+B2
A2=(B2+B3)//2 2*A2=B2+B3
A3=(B3+B1)//2 2*A3=B3+B1
2(A1-A2+A3)=B1+B2-B2-B3+B3+B1=2*B1
B1=A1-A2+A3
B2=2A1-B1
B3=2A2-B2

"""
