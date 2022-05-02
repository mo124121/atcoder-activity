A, B = input().split()
C = list(A)
D = list(B)

for i in range(3):
    if C[i] != "9":
        C[i] = "9"
        break
if D[0] != "1":
    D[0] = "1"
else:
    for i in range(1, 3):
        if D[i] != "0":
            D[i] = "0"
            break
print(max(int("".join(C)) - int(B), int(A) - int("".join(D))))
