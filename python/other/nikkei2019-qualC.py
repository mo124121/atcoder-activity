N = int(input())
A = [0] * N
B = [0] * N
D = []
for i in range(N):
    A[i], B[i] = map(int, input().split())
    D.append((A[i], B[i]))

C = [[((A[i] + B[i]), i) for i in range(N)] for s in [1, -1]]
C[0].sort()
C[1].sort()
ret = 0
c = 0
eaten = set()
while c < N and len(C[0]) + len(C[1]) > 0:
    _, i = C[c % 2].pop()
    if i not in eaten:
        eaten.add(i)
        ret += (-1) ** (c % 2) * D[i][c % 2]
        c += 1

print(ret)


"""
差をもっておいてソートして大きい順
すでに食べられてたらスキップ
"""
