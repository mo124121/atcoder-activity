N = int(input())

A = [1]
print(*A)
for i in range(1, N):
    line = [1]
    for j in range(1, i):
        line.append(A[j - 1] + A[j])
    line.append(1)
    A = line
    print(*A)
