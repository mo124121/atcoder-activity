A, B, W = map(int, input().split())

W *= 1000
mi = 10**9
mx = -1

for i in range(W // B, W // A + 1):
    if A * i <= W <= B * i:
        mi = min(mi, i)
        mx = max(mx, i)

if mx == -1:
    print("UNSATISFIABLE")
else:
    print(mi, mx)
