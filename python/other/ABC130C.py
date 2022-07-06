W, H, x, y = map(int, input().split())

area = W * H / 2

if x == W / 2 and y == H / 2:
    dupl = 1
else:
    dupl = 0

print(f"{area:.10f} {dupl}")
