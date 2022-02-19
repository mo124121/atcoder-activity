N = int(input())
t_bef, x_bef, y_bef = 0, 0, 0
flag = True
for i in range(N):
    t, x, y = map(int, input().split())
    t_diff = t - t_bef
    x_diff = abs(x - x_bef)
    y_diff = abs(y - y_bef)
    if t_diff < x_diff + y_diff:
        flag = False
    if (t_diff + x_diff + y_diff) % 2 != 0:
        flag = False
    t_bef, x_bef, y_bef = t, x, y
if flag:
    print("Yes")
else:
    print("No")
