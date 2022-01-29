N, v_a, v_b, L = map(int,input().split())
v_a = float(v_a)
v_b = float(v_b)
L = float(L)

for i in range(N):
    L = L * v_b / v_a

print("{:.6f}".format(L))
