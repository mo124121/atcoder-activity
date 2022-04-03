xr = 0
yr = 0
for i in range(3):
    x, y = map(int, input().split())
    xr ^= x
    yr ^= y
print(xr, yr)
