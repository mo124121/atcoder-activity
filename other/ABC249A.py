A, B, C, D, E, F, X = map(int, input().split())

t_c = X // (A + C)
t = t_c * A * B + B * min(A, max(0, (X - t_c * (A + C))))

a_c = X // (D + F)
a = a_c * D * E + E * min(D, max(0, (X - a_c * (D + F))))

if t == a:
    print("Draw")
elif t > a:
    print("Takahashi")
else:
    print("Aoki")
